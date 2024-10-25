class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
         int len=original.length;
        if(len!=m*n)
        {
            return new int[0][0];
        }
        
        int[][] twoD=new int[m][n];
        int k=0;
       
        for(int i=0;i<m;i++)
        {
          for(int j=0;j<n;j++)
          {
              twoD[i][j]=original[k++];
          } 
        }
        return twoD;
    }
}