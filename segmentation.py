#!/usr/bin/env python3

import numpy as np

def segregation(M, Ci, *varargin):
    """
    The degree to which edges are more dense within communities and more
    sparse between communities, which quantifies the segregation of a
    weighted network (Chan et al. 2014).

    Parameters:
    - M: weighted symmetrical matrix (n x n matrix)
    - Ci: community affiliation vector (n x 1 vector)
    - varargin: (Optional) 'diagzero' to convert diagonal to zero, 'negzero' to convert negative values to zero

    Returns:
    - S: System segregation calculated with W & B
    - W: Mean edge weight between nodes within the same community
    - B: Mean edge weight between nodes from different communities
    """
    # Check inputs
    if len(Ci) != M.shape[0]:
        raise ValueError('Length of label does not match with matrix dimension.')
    if len(varargin) > 2:
        raise ValueError('Too many optional inputs')
    nCi = np.unique(Ci)
    Wv = []
    Bv = []
    # Set diagonal/negatives to zero if specified
    if 'diagzero' in varargin:
        np.fill_diagonal(M, 0)
    if 'negzero' in varargin:
        M[M < 0] = 0
    for i in range(len(nCi)):  # loop through unique communities
        Wi = Ci == nCi[i]  # find index for within community edges
        Bi = Ci != nCi[i]  # find index for between community edges
        #print(' * Wi:',Wi.shape, Wi)
        #print(' * Bi:',Bi.shape, Bi)
        Wv_temp = M[Wi, :][:, Wi]  # extract within community edges
        Bv_temp = M[Wi, :][:, Bi]  # extract between community edges
        #print(' * Wv_temp:', Wv_temp.shape)
        ## matlab:  Wv = [Wv, Wv_temp(logical(triu(ones(sum(Wi)),1)))'];
        Wv.extend(Wv_temp[np.triu(np.ones_like(Wv_temp),k=1) == 1].flatten())
        Bv.extend(Bv_temp.flatten())
    W = np.mean(Wv)  # mean within community edges
    B = np.mean(Bv)  # mean between community edges
    S = (W - B) / W  # system segregation
    return S, W, B


def test(thresh=0.05, show_plots=False, debug=False):
    
    import bct
    from nilearn import plotting
    
    ts = np.loadtxt('data/sub-001_ses-1_Schaefer200x7_196v_ts.csv', delimiter=',')
    if debug:
        print(' + ts.shape:', ts.shape, ts[0][:5])
    
    ## compute correlation coefficients
    cc_r = np.corrcoef(ts, rowvar=False)
    if debug:
        print(' + cc_r.shape:', cc_r.shape, type(cc_r), cc_r[0][:5])
    
    ## z-score correlations
    cc_z = 0.5 * (np.log(1.+cc_r)-np.log(1.-cc_r))
    
    ## fill main diagonal with 0's
    np.fill_diagonal(cc_z, 0)

    if show_plots:
        plotting.plot_matrix(cc_z, colorbar=True, vmax=0.8, vmin=-0.8)
        plotting.show()
    
    ## apply proportional threshold
    cm = bct.threshold_proportional(cc_z, thresh)
    if debug:
        print(' + cm.shape:', cm.shape, type(cm), cm[0][:5])
    if show_plots:
        plotting.plot_matrix(cc_z, colorbar=True, vmax=0.8, vmin=-0.8)
        plotting.show()
    
    ## load network assigments for each node
    Ci = np.loadtxt('data/network_members.csv')
    if debug:
        print(' + Ci.shape:',Ci.shape, type(Ci))
    
    ## calculate segragation:
    S,W,B = segregation(cm, Ci)
    print(' ++ S:',S)
    print(' ++ W:',W)
    print(' ++ B:',B)
    return
