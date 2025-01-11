#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10250                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: freiheit517 <boj.kr/u/freiheit517>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10250                          #+#        #+#      #+#     #
#    Solved: 2024/08/15 18:08:20 by freiheit517   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
n = sys.stdin.readline()
for i in n:
  H, W, M = map(int,sys.stdin.readline().split())
  fl = M%H
  room = M//H + 1
  print(fl*100 +room)