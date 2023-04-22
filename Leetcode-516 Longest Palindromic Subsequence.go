func longestPalindromeSubseq(s string) int {
    arr:=make([][]int,len(s)+1)
    for i:=0;i<len(s)+1;i++{
        arr[i]=make([]int, len(s)+1)
    }

    for i:=1;i<len(s)+1;i++{
        for j:=1;j<len(s)+1;j++{
            if s[i-1]==s[len(s)-j]{
                arr[i][j]=arr[i-1][j-1]+1
            }else{
                if arr[i][j-1]>arr[i-1][j]{
                    arr[i][j]=arr[i][j-1]
                }else{
                    arr[i][j]=arr[i-1][j]
                }
            }
        }
    }

    return arr[len(s)][len(s)]
}
