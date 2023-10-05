import random

def gradDescVariableStep(funcGrad, func, x_0, a_0, eps, delt):
    x_k  = x_0
    f_x_k = func(xk)
    a_k = a_0
    
    while(vecNorm(f_x_k) > delt):
        x = vecAddvec(x_k, constMultVec(-a_k, funcGrad(x_k)))
        f_x = func(x)
        
        if(f_x - f_k_x > -a_k * eps * vecNorm(funcGrad(x_k))):
            a_k *= random.uniform(0.0, 1.0)
            continue
            
        x_k = x
        f_x_K = f_x
        
    return x_k

            