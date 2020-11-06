import pickle4reducer
import multiprocessing as multiprocessing
ctx = multiprocessing.get_context()
ctx.reducer = pickle4reducer.Pickle4Reducer()

def chunksize(n_workers, len_vnlist, factor):#(CPU_Count,len_vnf, 4)#4 is chosen as the data set is multiple of 4.
    chunksize, extra = divmod(len_vnlist, n_workers * factor)
    if extra:
        chunksize += 1
    return chunksize
#partial: using this multiple parameter can be passed to pool.map()
#chunksize: is fucn break the large data into chucks to utilise the avialable CPUs on running VM. 
#cpucount: by knowing CPU count you can utilise maximum of the VM.

def main():
	cpucount = multiprocessing.cpu_count() 
	pool = multiprocessing.Pool(cpucount)
	
	result_list = pool.map(partial(FucntionNeedtoCall,param1=param1,df=df,param2=param2,param3=param3,param14=param14),vnf_set,chunksize(cpucount, num, 4)) #
	pool.close()
	pool.join()