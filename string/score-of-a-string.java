class Solution {
    public int scoreOfString(String s) {
        int score = 0;
        int l = s.length()-1;
        for(int i=0; i<l; i++){
            score += Math.abs(s.charAt(i) - s.charAt(i+1));
        }
        return score;
    }
}