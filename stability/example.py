import numpy as np
import stability as stab


#normals = map(stab.normalize,
#              [np.array([[0, 0, 1]]).T,
#               np.array([[0, 0, 1]]).T,
#               np.array([[1, 0, 0]]).T])
#

def main():
  #normals = map(stab.normalize,
  #              [np.array([[-0.7, 0, 1]]).T,
  #               np.array([[0.1, 0.5, 1]]).T,
  #               np.array([[0.5, -0.5, 1]]).T])

  #pos = [np.array([[0, 0, 0]]).T,
  #       np.array([[0, 1, 0]]).T,
  #       np.array([[1, 0, 0.2]]).T]

  #normals = map(stab.normalize,
  #              [np.array([[0., 0., 1.]]).T,
  #               np.array([[0., 0., 1.]]).T,
  #               np.array([[0., 0., 1.]]).T,
  #               np.array([[0., 0., 1.]]).T])

  #pos = [np.array([[0.1, 0.155, -0.105]]).T,
  #       np.array([[-0.07, 0.155, -0.105]]).T,
  #       np.array([[-0.07, 0.055, -0.105]]).T,
  #       np.array([[0.1, 0.055, -0.105]]).T]

  normals = [np.array([[0, 0, 1]]).T]*3

  pos = [np.array([[0.1, 0, 0]]).T,
         np.array([[-0.1, 0, 0]]).T,
         np.array([[0.2, 0, 1]]).T]

  bar = sum(pos)/float(len(pos))
  pos = [p-bar for p in pos]

  mu = 0.5
  contacts = [stab.Contact(mu, p, n) for p, n in zip(pos, normals)]

  poly = stab.StabilityPolygon(60)
  poly.contacts = contacts

  poly.compute(1e-5, True, True, True, True)

main()
