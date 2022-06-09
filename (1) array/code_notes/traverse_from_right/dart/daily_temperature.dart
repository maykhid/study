void main() {
  print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]));
}

List<int> dailyTemperatures(List<int> T) {
  // keep track of numbers seen when you move left
  var list = <Map<int, int>>[];
  int n = T.length;
  var res = List.filled(n, 0);

  for (int i = n - 1; i >= 0; i--) {
    int curr = T[i];
    while (list.isNotEmpty && list.first.values.first <= curr) {
      list.removeAt(0);
    }
    res[i] = list.isEmpty ? 0 : list.first.keys.first - i;
    list.insert(0, {i: curr});
  }

  return res;
}

// Map<int, int> m = {1 : 1};
// List<int> dailyTemperatures(List<int> T) {
//   var n = T.length;
//   var right_max = -1.minInt;
//   List<int> result = List.filled(n, 0);

//   for (int i = n - 1; i > 0; i--) {
//     var t = T[i];
//     if (right_max <= t) {
//       right_max = t;
//     } else {
//       int days = 1;
//       while (T[i + days] <= t) {
//         days += result[i + days];
//       }
//       result[i] = days;
//     }
//   }
//   return result;
// }

// extension on int {
//   int get minInt =>
//       (double.infinity is int) ? -double.infinity as int : (-1 << 63);
// }

// List<int> dailyTemperatures(List<int> temperatures) {
//   var p1 = temperatures.length - 1;
//   var p2 = temperatures.length - 1;
//   var result = [];

//   if (p1 == temperatures.length - 1) {
//     result.add(0);
//     p1 -= 1;
//   }

//   while (p1 >= 0) {
//     // while (p1 < p2) {
//     // if (temperatures[p1] < temperatures[p2]) {
//     //   print(true);
//     //   p2--;
//     // } else if (temperatures[p1] > temperatures[p2]) {
//     //   result.insert(0, p2 + 1);
//     //   p1--;
//     //   print(result);
//     // } else {
//     //   result.insert(0, 0);
//     //   print(result);
//     //   p1--;
//     // }
//     // while (p2 >= p1) {
//     //   if (temperatures[p1] < temperatures[p2]) {
//     //     p2--;
//     //   } else {
//     //     result.insert(0, p2 + 1);
//     //   }
//     // }
//     // p1--;
//     while (p2 > p1) {
//       if (temperatures[p1] > temperatures[p2]) {
//         result.insert(0, p2 - p1);
//         // print('${temperatures[p2] - temperatures[p1]}');
//         print('on if $p2 - $p1');
//       }
//       // else if (temperatures[p1] < temperatures[p2]) {
//       //   result.insert(0, 0);
//       // }
//       else {
//         result.insert(0, 0);
//       }
//       p2--;
//     }
//     // p2 = temperatures.length - 1;
//     p1--;
//   }
//   // p1--;
//   // }
//   print(result);
//   return [];
// }
