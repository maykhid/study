// Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

// The test cases are generated so that the answer will fit in a 32-bit integer.

// A subarray is a contiguous subsequence of the array.

 

// Example 1:

// Input: nums = [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.
// Example 2:

// Input: nums = [-2,0,-1]
// Output: 0
// Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

// Constraints:

// 1 <= nums.length <= 2 * 104
// -10 <= nums[i] <= 10
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

import 'dart:math';

void main() {
  print(maxProduct([1, 2, 3, 4, 0, 5, 6, 3]));
}

int maxProduct(List<int> nums) {
  var maxi = (double.infinity is int) ? -double.infinity as int : (-1 << 63);
  var currentWindowProduct = 1;

  // forward
  for (var fromStart in nums) {
    currentWindowProduct *= fromStart;
    // maxi = max(currentWindowProduct, maxi);
    // maxi = max(maxi, fromStart);
    maxi = [currentWindowProduct, maxi, fromStart].reduce(max); // Finds max in an array
    if (currentWindowProduct == 0) {
      currentWindowProduct = 1;
    }
  }

  currentWindowProduct = 1;

  //  backward
  for (int fromEnd = nums.length - 1; fromEnd >= 0; fromEnd--) {
    currentWindowProduct *= nums[fromEnd];
    maxi = [currentWindowProduct, maxi, fromEnd].reduce(max);
    if (currentWindowProduct == 0) {
      currentWindowProduct = 1;
    }
  }
  return maxi;
}
