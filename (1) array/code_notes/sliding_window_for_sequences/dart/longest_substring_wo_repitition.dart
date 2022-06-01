import 'dart:math';

void main() {
  print(lengthOfLongestSubstring('abcabcbb'));
}

int lengthOfLongestSubstring(s) {
  var found = [];
  var substringCount = 0;
  var windowStart = 0;

  // if (s.length <= 2) {
  //   return substringCount;
  // }

  for (int i = 0; i < s.length; i++) {
    while (found.contains(s[i])) {
      found.remove(s[windowStart]);  // using the s[windowStart] acts like a slider
      windowStart++;
    }
    found.add(s[i]);
    substringCount = max(substringCount, found.length);
  }

  return substringCount;
}
