void main() {
  print(containsDuplicate([1, 2, 3, 2]));
}

// time O(n^2) space O(n)
// bool containsDuplicate(List<int> nums) { //0(1)
//   var found = []; // 0(1)
//   for (var i in nums) { // O(n)
//     if (found.contains(i)) { // O(n) * O(n)
//       return true;
//     }
//     found.add(i);
//   }
//   return false;
// }

// time O(n) space O(n)
bool containsDuplicate(List<int> nums) {
  return nums.length != nums.toSet().length;
}