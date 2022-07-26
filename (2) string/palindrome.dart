void main() {
  print(isPalindrome('day'));
}

bool isPalindrome(String s) {
  for (int i = 0, j = s.length - 1; i != s.length; i++, j--) {
    if (s[j] != s[i]) {
      return false;
    }
  }
  return true;
}
