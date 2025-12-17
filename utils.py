
def preprocess_h5ad(h5ad_path, do_norm_and_log1p=False):
    """
    Preprocess single-cell RNA-seq data from an H5AD file.
    
    Args:
        h5ad_path: Path to the input H5AD file containing AnnData object.
        do_norm_and_log1p: Whether to perform normalization and log1p transformation.
                           If False, assumes the data is already in `adata.X`.
                           If True, performs normalization and log1p, storing result in `adata.X`.
                           
    Returns:
        AnnData object with binned expression values stored in `adata.layers['X_binned']`.
        
    Notes:
        - Binning is always performed with 51 bins.
        - Binned values are stored in `adata.layers['X_binned']`.
        - If `do_norm_and_log1p=True`, the normalized and log1p-transformed data 
          replaces the original `adata.X`.
    """
    adata = sc.read_h5ad(h5ad_path)
    
    # Perform normalization and log1p transformation if requested
    # If already normalized, the values should be in adata.X directly
    if do_norm_and_log1p:
        do_normalizing_and_log1p(adata)
    
    # Perform binning with 51 bins
    # Binned values are stored in adata.layers['X_binned']
    do_binning(adata, 51)
    
    return adata
