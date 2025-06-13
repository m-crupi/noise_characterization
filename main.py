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



if __name__ == "__main__":
    main()