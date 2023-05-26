import faiss
print("===== faiss version =====")
print(faiss.__version__)

import numpy as np
print("===== numpy config =====")
np.__config__.show()


print("===== Run simple kmeans =====")
err = faiss.Kmeans(10, 20).train(numpy.random.rand(1000, 10).astype('float32'))
print(err)


print("==== Try other examples ====")
D, M, Ks = 32, 4, 256
Nt, Nb, Nq = 2000, 10000, 100
nbits = int(np.log2(Ks))
assert nbits == 8
Xt = np.random.rand(Nt, D).astype(np.float32)
Xb = np.random.rand(Nb, D).astype(np.float32)
Xq = np.random.rand(Nq, D).astype(np.float32)

pq = faiss.IndexPQ(D, M, nbits)
opq_matrix = faiss.OPQMatrix(D, M=M)
pq = faiss.IndexPreTransform(opq_matrix, pq)
pq.train(x=Xt)
pq.add(x=Xb)
