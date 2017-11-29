import numpy as np
import matplotlib.pyplot as plt


arr_3 = []
arr_6 = []
arr_24 = []
arr_48 = []

m_arr_3 = []
m_arr_6 = []
m_arr_24 = []
m_arr_48 = []


# ========3 ================

k = np.loadtxt("3_point51")
d = np.sort(k)
arr_3.append(np.percentile(d, 90))
print "with (3,1) and mean arrival rate = 1 , percentile = " + str(np.percentile(d, 90))
m_arr_3.append(np.mean(d))

k = np.loadtxt("3_11")
d = np.sort(k)
arr_3.append(np.percentile(d, 90))
m_arr_3.append(np.mean(d))
print "with (3,1) and mean arrival rate = 2 , percentile = " + str(np.percentile(d, 90))



k = np.loadtxt("3_21")
d = np.sort(k)
arr_3.append(np.percentile(d, 90))
m_arr_3.append(np.mean(d))


k = np.loadtxt("3_41")
d = np.sort(k)
arr_3.append(np.percentile(d, 90))
m_arr_3.append(np.mean(d))


k = np.loadtxt("3_81")
d = np.sort(k)
arr_3.append(np.percentile(d, 90))
m_arr_3.append(np.mean(d))


k = np.loadtxt("3_121")
d = np.sort(k)
arr_3.append(np.percentile(d, 90))
m_arr_3.append(np.mean(d))

k = np.loadtxt("3_141")
d = np.sort(k)
arr_3.append(np.percentile(d, 90))
m_arr_3.append(np.mean(d))


k = np.loadtxt("3_161")
d = np.sort(k)
arr_3.append(np.percentile(d, 90))
m_arr_3.append(np.mean(d))


# ==========6 =================

k = np.loadtxt("6_point51")
d = np.sort(k)
arr_6.append(np.percentile(d, 90))
m_arr_6.append(np.mean(d))

print "with (6,2) and mean arrival rate = 1 , percentile = " + str(np.percentile(d, 90))


k = np.loadtxt("6_11")
d = np.sort(k)
arr_6.append(np.percentile(d, 90))
m_arr_6.append(np.mean(d))

print "with (6,2) and mean arrival rate = 2 , percentile = " + str(np.percentile(d, 90))



k = np.loadtxt("6_21")
d = np.sort(k)
arr_6.append(np.percentile(d, 90))
m_arr_6.append(np.mean(d))


k = np.loadtxt("6_41")
d = np.sort(k)
arr_6.append(np.percentile(d, 90))
m_arr_6.append(np.mean(d))


k = np.loadtxt("6_81")
d = np.sort(k)
arr_6.append(np.percentile(d, 90))
m_arr_6.append(np.mean(d))


k = np.loadtxt("6_121")
d = np.sort(k)
arr_6.append(np.percentile(d, 90))
m_arr_6.append(np.mean(d))

k = np.loadtxt("6_141")
d = np.sort(k)
arr_6.append(np.percentile(d, 90))
m_arr_6.append(np.mean(d))



k = np.loadtxt("6_161")
d = np.sort(k)
arr_6.append(np.percentile(d, 90))
m_arr_6.append(np.mean(d))


#==========================24 =============


k = np.loadtxt("24_point51")
d = np.sort(k)
arr_24.append(np.percentile(d, 90))
m_arr_24.append(np.mean(d))

print "with (24,8) and mean arrival rate = 1 , percentile = " + str(np.percentile(d, 90))


k = np.loadtxt("24_11")
d = np.sort(k)
arr_24.append(np.percentile(d, 90))
m_arr_24.append(np.mean(d))




k = np.loadtxt("24_21")
d = np.sort(k)
arr_24.append(np.percentile(d, 90))
m_arr_24.append(np.mean(d))


k = np.loadtxt("24_41")
d = np.sort(k)
arr_24.append(np.percentile(d, 90))
m_arr_24.append(np.mean(d))


k = np.loadtxt("24_81")
d = np.sort(k)
arr_24.append(np.percentile(d, 90))
m_arr_24.append(np.mean(d))


k = np.loadtxt("24_121")
d = np.sort(k)
arr_24.append(np.percentile(d, 90))
m_arr_24.append(np.mean(d))

k = np.loadtxt("24_141")
d = np.sort(k)
arr_24.append(np.percentile(d, 90))
m_arr_24.append(np.mean(d))


k = np.loadtxt("24_161")
d = np.sort(k)
arr_24.append(np.percentile(d, 90))
m_arr_24.append(np.mean(d))

x_axis = [1,2,4,8,16,24,28,32]


plt.plot(x_axis, arr_3, label="3,1")
plt.plot(x_axis, arr_6, label = "6,2")
plt.plot(x_axis, arr_24, label = "24,8")


plt.legend(['(3,1)', '(6,2)', '(24,8)'], loc='upper left')
plt.grid(which="minor", axis="y")
plt.minorticks_on()


plt.xlabel("Mean Arrival rate")
plt.ylabel("90th percentile")
plt.tight_layout()

plt.show()


# ========================== 48 =========

#
#
#
# k = np.loadtxt("6_11")
# d = np.sort(k)
#
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("24_11")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
#
# k = np.loadtxt("48_11")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
#
# k = np.loadtxt("3_21")
# d = np.sort(k)
#
# print np.percentile(d, 90)
#
# k = np.loadtxt("6_21")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("24_21")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("48_21")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("3_41")
# d = np.sort(k)
#
# print np.percentile(d, 90)
#
#
#
# k = np.loadtxt("6_41")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("24_41")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
#
# k = np.loadtxt("48_41")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
#
# k = np.loadtxt("8_81")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("24_81")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
#
# k = np.loadtxt("48_81")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("6_121")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("24_121")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("48_121")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
#
# k = np.loadtxt("6_141")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("24_141")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("48_141")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("6_161")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
#
# k = np.loadtxt("24_161")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("48_161")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
# k = np.loadtxt("3_161")
# d = np.sort(k)
#
# #print np.mean(d)
# print np.percentile(d, 90)
#
#
#
# #
# # k = np.loadtxt("experiement_point_2/M_6_2_point_200001")
# # d = np.sort(k)
# #
# # #print np.mean(d)
# # print np.percentile(d, 99)
# #
# # k = np.loadtxt("experiement_point_2/M_24_8_point_200001")
# # d = np.sort(k)
# #
# # print np.mean(d)
# # print np.percentile(d, 99)
#
#
# # k = np.loadtxt("experiement_point_2/24_8_point10001")
# # d = np.sort(k)
# #
# # print np.mean(d)
# print np.percentile(d, 80)