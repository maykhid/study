void main() {
  print(merge([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3));
}

// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

merge(List nums1, List nums2, m, n) {
  var i = 0;
  var j = 0;
  var merged = [];

  if (nums1.length > m) {
    nums1.removeRange((i + m).toInt(), nums1.length);
  }
  if (nums2.length > n) {
    nums2.removeRange((j + n).toInt(), nums2.length);
  }

  while (i < m && j < n) {
    // print(nums1);
    if (nums1[i] < nums2[j]) {
      merged.add(nums1[i]);
      i += 1;
    } else {
      merged.add(nums2[j]);
      j += 1;
    }
  }

  merged
    ..addAll(nums1.sublist(i))
    ..addAll(nums2.sublist(j));
  print(merged);
}
