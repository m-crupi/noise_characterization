from src.optimizer import *

def main():
    # Some example of unitaries
    Id = np.eye(2)
    CNOT = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 0, 1],[0, 0, 1, 0]])
    iSWAP = np.array([[1,0,0,0],[0,0,1j,0],[0,1j,0,0],[0,0,0,1]])

    # example of entry to estimate
    alpha = [1,0]
    beta = [0,0]
    ind = index_to_lst_alpha_beta(alpha,beta) #converts the indexes alpha and beta to a single index

    # computing the optimal function g and minimized value for the corresponding entry
    g,val = g_entry_optimal(CNOT,ind)

    # Please note that the g is constructed as a 2d array. The first axes corresponds to (alpha,beta) while the second corresponds to (r,s)
    # To help visualize the matrix elements corresponding to the desired (alpha,beta) and (r,s) you can use the following functions:
    # list_to_index_alpha_beta(alpha,beta)
    # index_to_lst_alpha_beta (index,n)
    # list_to_index_r_s (r,s)
    # index_to_lst_r_s (index,n)



if __name__ == "__main__":
    main()