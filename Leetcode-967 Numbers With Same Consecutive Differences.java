class Solution {
    static ArrayList<Integer> arr;
    public void go(int i,String s,int rem,int k){
        if(rem==0){
            Solution.arr.add(Integer.parseInt(s));
            return;
        }
        if(i+k<10)
            go(i+k,s+Integer.toString(i+k),rem-1,k);
        
        if(k!=0 && i-k>-1)
            go(i-k,s+Integer.toString(i-k),rem-1,k);
        return;
    }
    
    public int[] numsSameConsecDiff(int n, int k) {
        Solution.arr=new ArrayList<>();
        
        for(int i=1;i<10;i++)
            go(i,Integer.toString(i),n-1,k);
        return Solution.arr.stream().mapToInt(i -> i).toArray();
        
    }
}
