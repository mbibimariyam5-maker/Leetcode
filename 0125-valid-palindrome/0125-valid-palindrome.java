class Solution {
    public boolean isPalindrome(String s) {
        String ans ="";
        for(int i=0;i < s.length();i++)
        {
            char ch = s.charAt(i);
            if((ch >= 'a' && ch <= 'z') ||( ch >= 'A' && ch <= 'Z' )|| (ch >= '0' && ch<='9'))
            ans = ans + ch;
            
        }
        ans = ans.toLowerCase();

        int left = 0;
        int right = ans.length() - 1;

        while (left < right) {
            
            while (left < right && !Character.isLetterOrDigit(ans.charAt(left))) {
                left++;
            }
    
            while (left < right && !Character.isLetterOrDigit(ans.charAt(right))) {
                right--;
            }

            
            if (Character.toLowerCase(ans.charAt(left)) != Character.toLowerCase(ans.charAt(right))) {
                return false;
            }

            left++;
            right--;
        }

        return true;

        
    }
}