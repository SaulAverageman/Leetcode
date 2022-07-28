func isAnagram(s string, t string) bool {
    return arrayfy(s)==arrayfy(t);
}

func arrayfy(s string) [26]int {
    var arr[26] int;
    for i:=0;i<len(s);i++ {
        chr:=int(s[i]);
        arr[int(chr)-97]+=1;
    }
    return arr;
}
