def normalization(x, dl, dh, nl, nh):
    return (float((x-dl)*(nh-nl))/(dh-dl))-dl
