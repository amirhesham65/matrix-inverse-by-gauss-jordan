class Matrix:
    def __init__(self, mat):
        self.mat = mat

    # A handy method to print the matrix to the console
    def print(self):
        for i in self.mat:
            for j in i:
                print(j, end=" ")
            print('')

    # Adding the identity matrix to the original matrix from the right (Augmenting the matrix)
    def add_identity_matrix(self):
        n = len(self.mat)
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.mat[i].append(1)
                else:
                    self.mat[i].append(0)
        return self.mat

    # Removing the identity matrix - after inverting - from the left
    def remove_identity_matrix(self):
        n = len(self.mat)
        new_mat = []
        for i in range(n):
            new_mat.append(self.mat[i][n:])
        self.mat = new_mat

    # Inverting the matrix
    # NOTE: this program assumes the given matrix is already invertible and non-singular
    # for more info: https://mathworld.wolfram.com/NonsingularMatrix.html
    def inverse(self):
        n = len(self.mat)

        # Handling the 2x2 matrix inverse
        if n == 2:
            det = self.mat[0][0]*self.mat[1][1] - self.mat[0][1]*self.mat[1][0]
            new_mat = [
                [self.mat[1][1], -self.mat[0][1]],
                [-self.mat[1][0], self.mat[0][0]]
            ]
            for i in range(n):
                for j in range(n):
                    new_mat[i][j] /= det
            self.mat = new_mat
            return

        aug_mat = self.add_identity_matrix()

        for i in range(n):
            pivot = aug_mat[i][i]

            for a in range(2 * n):
                aug_mat[i][a] = aug_mat[i][a] / pivot

            for j in range(n):
                if j != i:
                    pivot = aug_mat[i][i]
                    target = aug_mat[j][i]
                    ratio = -target / pivot
                    for k in range(2 * n):
                        aug_mat[j][k] = ratio * aug_mat[i][k] + aug_mat[j][k]
        self.remove_identity_matrix()