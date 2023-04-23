func numberOfArrays(s string, k int) int {
    arr:=make([]int,len(s)+1)
    arr[0]=1
    BIG:=1000000007

    for i:=1;i<len(s)+1;i++{
        col:=""
        col+=string(s[i-1])
        coli,_:=strconv.Atoi(col)
        if coli>0 && coli<=k{
            arr[i]=arr[i-1]
        }else if coli>k{
            return 0
        }

        for j:=i-1;j>0;j--{
            if arr[j]==0{
                return 0
            }
            x,_:=strconv.Atoi(string(s[j-1]))
            coli=int(math.Pow(float64(10),float64(i-j)))*x+coli
            if x==0{
                continue
            }
            if coli>k{
                break
            }
            arr[i]+=arr[j-1]
            arr[i]%=BIG
        }
    }
    return arr[len(arr)-1]
}
