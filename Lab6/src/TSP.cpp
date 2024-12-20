#include "TSP.hpp"

#include <algorithm>
#include <stack>
#include <optional>

std::ostream& operator<<(std::ostream& os, const CostMatrix& cm) {
    for (std::size_t r = 0; r < cm.size(); ++r) {
        for (std::size_t c = 0; c < cm.size(); ++c) {
            const auto& elem = cm[r][c];
            os << (is_inf(elem) ? "INF" : std::to_string(elem)) << " ";
        }
        os << "\n";
    }
    os << std::endl;

    return os;
}

/* PART 1 */

/**
 * Create path from unsorted path and last 2x2 cost matrix.
 * @return The vector of consecutive vertex.
 */
path_t StageState::get_path() {
    NewVertex last_vertex = choose_new_vertex();
    append_to_path(last_vertex.coordinates);
    update_cost_matrix(last_vertex.coordinates);

    for(std::size_t i = 0; i < matrix_.size(); i++)
    {
        for(std::size_t j = 0; j < matrix_.size(); j++)
        {
            if(matrix_[i][j] != INF)
                append_to_path(vertex_t(i, j));
        }
    }

    path_t sorted_path = {unsorted_path_[0].col};
    unsorted_path_[0].row = INF;

    while(sorted_path.size() != unsorted_path_.size())
    {
        for(auto& elem: unsorted_path_)
        {
            if(elem.row == sorted_path.back())
            {
                sorted_path.push_back(elem.col);
                elem.row = INF;
            }
        }
    }
    return sorted_path;
}

/**
 * Get minimum values from each row and returns them.
 * @return Vector of minimum values in row.
 */
std::vector<cost_t> CostMatrix::get_min_values_in_rows() const 
{
    std::vector<cost_t> min_values = {};
    for(const auto& row:matrix_)
    {
        auto x = std::min_element(row.begin(), row.end());
        min_values.push_back(*x);
    }

    std::replace(min_values.begin(), min_values.end(), INF, 0);

    return min_values;
}

/**
 * Reduce rows so that in each row at least one zero value is present.
 * @return Sum of values reduced in rows.
 */
cost_t CostMatrix::reduce_rows() {
    std::vector<cost_t> min_values = get_min_values_in_rows();

    auto it_min_start = min_values.begin(); 
    auto it_min_end = min_values.end(); 
    
    size_t matrix_size = size();
    
    for (size_t row = 0; row < matrix_size; ++row)
    {
        for(auto& col:matrix_[row])
        {
            if(col != INF)
                col -= min_values[row];
        }
    }
    
    return std::accumulate(it_min_start, it_min_end, 0);
}

/**
 * Get minimum values from each column and returns them.
 * @return Vector of minimum values in columns.
 */
std::vector<cost_t> CostMatrix::get_min_values_in_cols() const {
    size_t matrix_size = size();

    std::vector<cost_t> min_values(matrix_size, INF);

    for (size_t col = 0; col < matrix_size; ++col) 
    {
        for (const auto& row:matrix_) 
        {
            min_values[col] = std::min(min_values[col], row[col]);
        }
    }    
    std::replace(min_values.begin(), min_values.end(), INF, 0);

    return min_values;
}

/**
 * Reduces rows so that in each column at least one zero value is present.
 * @return Sum of values reduced in columns.
 */
cost_t CostMatrix::reduce_cols() {
    std::vector<cost_t> min_values = get_min_values_in_cols();

    
    auto it_min_start = min_values.begin(); 
    auto it_min_end = min_values.end(); 

    std::vector<cost_t>::iterator it_row;
    std::vector<cost_t>::iterator it_min;

    for(auto& row : matrix_)
    {
        for(it_min = it_min_start, it_row = row.begin(); it_min < it_min_end; it_row++, it_min++)
        {
            if( *it_row != INF)
                *it_row -= *it_min;
        }
    }

    return std::accumulate(it_min_start, it_min_end, 0);
}

/**
 * Get the cost of not visiting the vertex_t (@see: get_new_vertex())
 * @param row
 * @param col
 * @return The sum of minimal values in row and col, excluding the intersection value.
 */
cost_t CostMatrix::get_vertex_cost(std::size_t row, std::size_t col) const {
    cost_t min_row_val = INF;
    cost_t min_col_val = INF;

    size_t matrix_size = size();

    // Min row value:
    for(std::size_t r = 0; r < matrix_size; ++r)
    {
        if(r != col)
            min_row_val = std::min(min_row_val, matrix_[row][r]);
    }

    // Min col value
    for(std::size_t c = 0; c < matrix_size; ++c)
    {
        if(c != row)
            min_col_val = std::min(min_col_val, matrix_[c][col]);
    }

    return min_col_val + min_row_val;
}

/* PART 2 */

/**
 * Choose next vertex to visit:
 * - Look for vertex_t (pair row and column) with value 0 in the current cost matrix.
 * - Get the vertex_t cost (calls get_vertex_cost()).
 * - Choose the vertex_t with maximum cost and returns it.
 * @param cm
 * @return The coordinates of the next vertex.
 */
NewVertex StageState::choose_new_vertex() {
    std::size_t matrix_size = matrix_.size();
    vertex_t vertex;
    
    cost_t max_cost = -1;
    cost_t cost = -1;
    
    for(std::size_t r = 0; r < matrix_size; ++r) 
    {
        for(std::size_t c = 0; c < matrix_size; ++c) 
        {
            if(matrix_[r][c] == 0)
            {
                cost = matrix_.get_vertex_cost(r, c);
                if(cost > max_cost)
                {
                    max_cost = cost;
                    vertex = vertex_t{r,c};
                }
            }
        }   
    }

    return NewVertex(vertex, max_cost);
}

/**
 * Update the cost matrix with the new vertex.
 * @param new_vertex
 */
void StageState::update_cost_matrix(vertex_t new_vertex) {
    
    std::size_t matrix_size = matrix_.size();

    // Block values in new_vertex cols and rows    
    for(std::size_t col = 0; col < matrix_size; ++col)
    {
        matrix_[col][new_vertex.col] = INF;
    }
    for(std::size_t row = 0; row < matrix_size; ++row)
    {
        matrix_[new_vertex.row][row] = INF;
    }        
    
    // avoiding self loop
    matrix_[new_vertex.col][new_vertex.row] = INF;

    // case of not closing loop before last one
    if(unsorted_path_.size() != matrix_size)
    {
        matrix_[new_vertex.col][unsorted_path_.back().row] = INF;

        std::vector<std::pair<std::size_t, bool>> v_from = {};
        std::vector<std::pair<std::size_t, bool>> v_to = {};

        for(auto& edge: unsorted_path_)
        {
            v_from.push_back(std::make_pair(edge.row, false));
            v_to.push_back(std::make_pair(edge.col, false));
        }

        for(std::size_t i = 0; i < v_from.size(); i++)
        {
            for(std::size_t j = i; j < v_from.size(); j++)
            {
                if(v_from[i] == v_from[j] && i != j)
                    v_from[i].second = v_from[j].second = true;
                
                if(v_to[i] == v_to[j] && i != j)
                    v_to[i].second = v_to[j].second = true;
            } 
        }           
    } 
    return;    
}

/**
 * Reduce the cost matrix.
 * @return The sum of reduced values.
 */
cost_t StageState::reduce_cost_matrix() 
{
    cost_t sum_reduced_row_values = matrix_.reduce_rows();
    cost_t sum_reduced_col_values = matrix_.reduce_cols();

    return sum_reduced_col_values + sum_reduced_row_values;    
}

/**
 * Given the optimal path, return the optimal cost.
 * @param optimal_path
 * @param m
 * @return Cost of the path.
 */
cost_t get_optimal_cost(const path_t& optimal_path, const cost_matrix_t& m) 
{
    cost_t cost = 0;

    for (std::size_t idx = 1; idx < optimal_path.size(); ++idx) {
        cost += m[optimal_path[idx - 1]][optimal_path[idx]];
    }

    // Add the cost of returning from the last city to the initial one.
    cost += m[optimal_path[optimal_path.size() - 1]][optimal_path[0]];

    return cost;
}

/**
 * Create the right branch matrix with the chosen vertex forbidden and the new lower bound.
 * @param m
 * @param v
 * @param lb
 * @return New branch.
 */
StageState create_right_branch_matrix(cost_matrix_t m, vertex_t v, cost_t lb) {
    CostMatrix cm(m);
    cm[v.row][v.col] = INF;
    return StageState(cm, {}, lb);
}

/**
 * Retain only optimal ones (from all possible ones).
 * @param solutions
 * @return Vector of optimal solutions.
 */
tsp_solutions_t filter_solutions(tsp_solutions_t solutions) {
    cost_t optimal_cost = INF;
    for (const auto& s : solutions) {
        optimal_cost = (s.lower_bound < optimal_cost) ? s.lower_bound : optimal_cost;
    }

    tsp_solutions_t optimal_solutions;
    std::copy_if(solutions.begin(), solutions.end(),
                 std::back_inserter(optimal_solutions),
                 [&optimal_cost](const tsp_solution_t& s) { return s.lower_bound == optimal_cost; }
    );

    return optimal_solutions;
}

/**
 * Solve the TSP.
 * @param cm The cost matrix.
 * @return A list of optimal solutions.
 */
tsp_solutions_t solve_tsp(const cost_matrix_t& cm) {

    StageState left_branch(cm);

    // The branch & bound tree.
    std::stack<StageState> tree_lifo;

    // The number of levels determines the number of steps before obtaining
    // a 2x2 matrix.
    std::size_t n_levels = cm.size() - 2;

    tree_lifo.push(left_branch);   // Use the first cost matrix as the root.

    cost_t best_lb = INF;
    tsp_solutions_t solutions;

    while (!tree_lifo.empty()) {

        left_branch = tree_lifo.top();
        tree_lifo.pop();

        while (left_branch.get_level() != n_levels && left_branch.get_lower_bound() <= best_lb) {
            // Repeat until a 2x2 matrix is obtained or the lower bound is too high...

            if (left_branch.get_level() == 0) {
                left_branch.reset_lower_bound();
            }

            // 1. Reduce the matrix in rows and columns.
            cost_t new_cost = 0; // @TODO (KROK 1)
            new_cost = left_branch.reduce_cost_matrix();

            // 2. Update the lower bound and check the break condition.
            left_branch.update_lower_bound(new_cost);
            if (left_branch.get_lower_bound() > best_lb) {
                break;
            }

            // 3. Get new vertex and the cost of not choosing it.
            NewVertex new_vertex = NewVertex(); // @TODO (KROK 2)
            new_vertex = left_branch.choose_new_vertex();

            // 4. @TODO Update the path - use append_to_path method.
            left_branch.append_to_path(new_vertex.coordinates);

            // 5. @TODO (KROK 3) Update the cost matrix of the left branch.
            left_branch.update_cost_matrix(new_vertex.coordinates);

            // 6. Update the right branch and push it to the LIFO.
            cost_t new_lower_bound = left_branch.get_lower_bound() + new_vertex.cost;
            tree_lifo.push(create_right_branch_matrix(cm, new_vertex.coordinates,
                                                      new_lower_bound));
        }

        if (left_branch.get_lower_bound() <= best_lb) {
            // If the new solution is at least as good as the previous one,
            // save its lower bound and its path.
            best_lb = left_branch.get_lower_bound();
            path_t new_path = left_branch.get_path();
            solutions.push_back({get_optimal_cost(new_path, cm), new_path});
        }
    }

    return filter_solutions(solutions); // Filter solutions to find only optimal ones.
}
