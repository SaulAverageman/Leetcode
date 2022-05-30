class Solution {
    public int divide(int Dividend, int Divisor) {
        long out=0;
        int neg=0;
        long dividend=Dividend,divisor=Divisor;
        if (dividend<0){
            neg+=1;
            dividend=-dividend;
        }
        
        if (divisor<0){
            neg+=1;
            divisor=-divisor;
        }
        long d=divisor,prev=dividend;
        System.out.println(""+dividend+" "+divisor+" "+neg);
        while (d<=dividend){
            int col=0;
            while(dividend>=divisor){
                //System.out.println(""+dividend+" "+divisor+" "+col);
                prev=divisor;
                divisor+=divisor;
                col+=1;
            }
            dividend-=prev;
            divisor=d;
            
            long j=1;
            for (long i=0;i<col-1;i++)
                j+=j;
            out+=j;
        }
        
        if (neg==0 || neg==2){
            if (out==(long)Integer.MAX_VALUE+1)
                out-=1;
            return (int)out;
    }
        return (int)-out;
    }   
}