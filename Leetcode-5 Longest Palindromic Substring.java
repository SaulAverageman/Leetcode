class Solution {
    public void ss(int i,int n,int[] req){
            if (n%2==0)
                req[0]=i-n/2+1;
            else
                req[0]=i-n/2;
            
            req[1]=i+n/2+1;
        }
    public String longestPalindrome(String s) {
        int req[]=new int[]{0,0};
        
        int out=0;
        int l1=s.length()+1;
        int ll[][]= new int[l1][l1];
        for (int i=l1-1;i>0;i--){
            for(int j=1;j<=i;j++){
                if (i==j)
                    ll[l1-i][j]=ll[l1-i-1][j-1]+1;
                else if (s.charAt(j-1)==s.charAt(i-1))
                    ll[l1-i][j]=ll[l1-i-1][j-1]+2;
                
                if (ll[l1-i][j]>out && (i==j+1 || i==j)){
                    out=ll[l1-i][j];
                    ss(j-1,ll[l1-i][j],req);
                }
            //System.out.print(ll[i][j]);
            }
        //System.out.println();
        }
        
        return s.substring(req[0],req[1]);
    }
}
