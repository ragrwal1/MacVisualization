import re
import matplotlib.pyplot as plt
import numpy as np
import mplcursors
import seaborn as sns




# Sample raw input data
raw_data = """
Mac Studio (2023)
Apple M2 Ultra @ 3.7 GHz (24 CPU cores, 60 GPU cores)
21329	
 
Mac Studio (2023)
Apple M2 Ultra @ 3.7 GHz (24 CPU cores, 76 GPU cores)
21329	
 
Mac Pro (2023)
Apple M2 Ultra @ 3.7 GHz (24 CPU cores, 60 GPU cores)
21206	
 
Mac Pro (2023)
Apple M2 Ultra @ 3.7 GHz (24 CPU cores, 76 GPU cores)
21206	
 
MacBook Pro (16-inch, Nov 2023)
Apple M3 Max @ 4.1 GHz (16 CPU cores, 40 GPU cores)
20957	
 
MacBook Pro (14-inch, Nov 2023)
Apple M3 Max @ 4.1 GHz (16 CPU cores, 40 GPU cores)
20904	
 
MacBook Pro (14-inch, Nov 2023)
Apple M3 Max @ 4.1 GHz (14 CPU cores, 30 GPU cores)
18964	
 
MacBook Pro (16-inch, Nov 2023)
Apple M3 Max @ 4.1 GHz (14 CPU cores, 30 GPU cores)
18955	
 
Mac Studio (2022)
Apple M1 Ultra @ 3.2 GHz (20 cores)
17964	
 
MacBook Pro (16-inch, Nov 2023)
Apple M3 Pro @ 4.1 GHz (12 CPU cores, 18 GPU cores)
15288	
 
MacBook Pro (14-inch, Nov 2023)
Apple M3 Pro @ 4.1 GHz (12 CPU cores, 18 GPU cores)
15268	
 
Mac Studio (2023)
Apple M2 Max @ 3.7 GHz (12 CPU cores, 30 GPU cores)
14802	
 
Mac Studio (2023)
Apple M2 Max @ 3.7 GHz (12 CPU cores, 38 GPU cores)
14802	
 
MacBook Pro (16-inch, 2023)
Apple M2 Max @ 3.7 GHz (12 CPU cores, 30 GPU cores)
14534	
 
MacBook Pro (16-inch, 2023)
Apple M2 Max @ 3.7 GHz (12 CPU cores, 38 GPU cores)
14534	
 
Mac mini (2023)
Apple M2 Pro @ 3.5 GHz (12 CPU cores, 19 GPU cores)
14298	
 
MacBook Pro (14-inch, 2023)
Apple M2 Pro @ 3.5 GHz (12 CPU cores, 19 GPU cores)
14252	
 
MacBook Pro (16-inch, 2023)
Apple M2 Pro @ 3.5 GHz (12 CPU cores, 19 GPU cores)
14202	
 
MacBook Pro (14-inch, Nov 2023)
Apple M3 Pro @ 4.1 GHz (11 CPU cores, 14 GPU cores)
14021	
 
Mac Studio (2022)
Apple M1 Max @ 3.2 GHz (10 cores)
12488	
 
MacBook Pro (14-inch, 2021)
Apple M1 Pro @ 3.2 GHz (10 cores)
12257	
 
MacBook Pro (14-inch, 2021)
Apple M1 Max @ 3.2 GHz (10 cores)
12257	
 
MacBook Pro (16-inch, 2021)
Apple M1 Pro @ 3.2 GHz (10 CPU cores, 10 GPU cores)
12219	
 
MacBook Pro (16-inch, 2021)
Apple M1 Max @ 3.2 GHz (10 cores)
12219	
 
Mac mini (2023)
Apple M2 Pro @ 3.5 GHz (10 CPU cores, 16 GPU cores)
12185	
 
MacBook Pro (14-inch, 2023)
Apple M2 Pro @ 3.5 GHz (10 CPU cores, 16 GPU cores)
12143	
 
iMac (24-inch, 2023)
Apple M3 @ 4.1 GHz (8 CPU cores, 10 GPU cores)
11704	
 
iMac (24-inch, 2023)
Apple M3 @ 4.1 GHz (8 CPU cores, 8 GPU cores)
11696	
 
MacBook Pro (14-inch, Nov 2023)
Apple M3 @ 4.1 GHz (8 CPU cores, 10 GPU cores)
11593	
 
Mac Pro (Late 2019)
Intel Xeon W-3275M @ 2.5 GHz (28 cores)
10571	
 
MacBook Pro (14-inch, 2021)
Apple M1 Pro @ 3.2 GHz (8 cores)
10322	
 
Mac Pro (Late 2019)
Intel Xeon W-3245 @ 3.2 GHz (16 cores)
10286	
 
Mac Pro (Late 2019)
Intel Xeon W-3265M @ 2.7 GHz (24 cores)
9807	
 
Mac mini (2023)
Apple M2 @ 3.5 GHz (8 CPU cores, 10 GPU cores)
9758	
 
MacBook Air (15-inch, 2023)
Apple M2 @ 3.5 GHz (8 CPU cores, 10 GPU cores)
9744	
 
iMac Pro (Late 2017)
Intel Xeon W-2191B @ 2.3 GHz (18 cores)
9678	
 
MacBook Air (2022)
Apple M2 @ 3.5 GHz (8 cores)
9655	
 
MacBook Pro (13-inch, 2022)
Apple M2 @ 3.5 GHz (8 cores)
9643	
 
Mac Pro (Late 2019)
Intel Xeon W-3235 @ 3.3 GHz (12 cores)
9376	
 
iMac Pro (Late 2017)
Intel Xeon W-2170B @ 2.5 GHz (14 cores)
8812	
 
Mac mini (Late 2020)
Apple M1 @ 3.2 GHz (8 cores)
8414	
 
iMac (24-inch Mid 2021)
Apple M1 @ 3.2 GHz (8 cores)
8333	
 
iMac (24-inch Mid 2021)
Apple M1 @ 3.2 GHz (8 cores)
8333	
 
MacBook Air (Late 2020)
Apple M1 @ 3.2 GHz (8 CPU cores, 8 GPU cores)
8319	
 
MacBook Air (Late 2020)
Apple M1 @ 3.2 GHz (8 CPU cores, 7 GPU cores)
8319	
 
iMac (27-inch Retina Mid 2020)
Intel Core i9-10910 @ 3.6 GHz (10 cores)
8183	
 
MacBook Pro (13-inch Late 2020)
Apple M1 @ 3.2 GHz (8 cores)
8096	
 
iMac Pro (Late 2017)
Intel Xeon W-2150B @ 3.0 GHz (10 cores)
8073	
 
iMac (27-inch Retina Mid 2020)
Intel Core i7-10700K @ 3.8 GHz (8 cores)
7696	
 
iMac (27-inch Retina Early 2019)
Intel Core i9-9900K @ 3.6 GHz (8 cores)
7652	
 
iMac Pro (Late 2017)
Intel Xeon W-2140B @ 3.2 GHz (8 cores)
7345	
 
Mac Pro (Late 2019)
Intel Xeon W-3223 @ 3.5 GHz (8 cores)
7202	
 
MacBook Pro (16-inch Late 2019)
Intel Core i9-9980HK @ 2.4 GHz (8 cores)
6413	
 
iMac (27-inch Retina Mid 2020)
Intel Core i5-10600 @ 3.3 GHz (6 cores)
6306	
 
MacBook Pro (15-inch Mid 2019)
Intel Core i9-9980HK @ 2.4 GHz (8 cores)
6273	
 
MacBook Pro (15-inch Mid 2019)
Intel Core i9-9980HK @ 2.4 GHz (8 cores)
6273	
 
MacBook Pro (16-inch Late 2019)
Intel Core i9-9880H @ 2.3 GHz (8 cores)
6230	
 
iMac (21.5-inch Retina Early 2019)
Intel Core i7-8700 @ 3.2 GHz (6 cores)
6157	
 
iMac (27-inch Retina Mid 2020)
Intel Core i5-10500 @ 3.1 GHz (6 cores)
6065	
 
MacBook Pro (15-inch Mid 2019)
Intel Core i9-9880H @ 2.3 GHz (8 cores)
5962	
 
Mac mini (Late 2018)
Intel Core i7-8700B @ 3.2 GHz (6 cores)
5565	
 
iMac (27-inch Retina Early 2019)
Intel Core i5-9600K @ 3.7 GHz (6 cores)
5464	
 
MacBook Pro (16-inch Late 2019)
Intel Core i7-9750H @ 2.6 GHz (6 cores)
5221	
 
iMac (27-inch Retina Early 2019)
Intel Core i5-8600 @ 3.1 GHz (6 cores)
5204	
 
MacBook Pro (15-inch Mid 2018)
Intel Core i9-8950HK @ 2.9 GHz (6 cores)
5077	
 
MacBook Pro (15-inch Mid 2019)
Intel Core i7-9750H @ 2.6 GHz (6 cores)
5070	
 
iMac (21.5-inch Retina Early 2019)
Intel Core i5-8500 @ 3.0 GHz (6 cores)
4988	
 
iMac (27-inch Retina Early 2019)
Intel Core i5-8500 @ 3.0 GHz (6 cores)
4945	
 
MacBook Pro (15-inch Mid 2018)
Intel Core i7-8850H @ 2.6 GHz (6 cores)
4907	
 
Mac Pro (Late 2013)
Intel Xeon E5-2697 v2 @ 2.7 GHz (12 cores)
4888	
 
Mac mini (Late 2018)
Intel Core i5-8500B @ 3.0 GHz (6 cores)
4863	
 
iMac (27-inch Retina Mid 2017)
Intel Core i7-7700K @ 4.2 GHz (4 cores)
4858	
 
MacBook Pro (15-inch Mid 2018)
Intel Core i7-8750H @ 2.2 GHz (6 cores)
4834	
 
iMac (21.5-inch Retina Mid 2017)
Intel Core i7-7700 @ 3.6 GHz (4 cores)
4609	
 
MacBook Pro (13-inch Mid 2019)
Intel Core i7-8569U @ 2.8 GHz (4 cores)
4518	
 
iMac (27-inch Retina Late 2015)
Intel Core i7-6700K @ 4.0 GHz (4 cores)
4388	
 
MacBook Pro (13-inch Mid 2020)
Intel Core i5-1038NG7 @ 2.0 GHz (4 cores)
4363	
 
Mac Pro (Late 2013)
Intel Xeon E5-1680 v2 @ 3.0 GHz (8 cores)
4330	
 
MacBook Pro (13-inch Mid 2018)
Intel Core i7-8559U @ 2.7 GHz (4 cores)
4306	
 
MacBook Pro (13-inch Mid 2020)
Intel Core i7-1068NG7 @ 2.3 GHz (4 cores)
4240	
 
MacBook Pro (13-inch Mid 2019)
Intel Core i5-8279U @ 2.4 GHz (4 cores)
4124	
 
MacBook Pro (13-inch Mid 2019)
Intel Core i7-8557U @ 1.7 GHz (4 cores)
4117	
 
iMac (21.5-inch Retina Late 2015)
Intel Core i7-5775R @ 3.3 GHz (4 cores)
4088	
 
iMac (27-inch Retina)
Intel Core i7-4790K @ 4.0 GHz (4 cores)
4060	
 
MacBook Pro (13-inch Mid 2018)
Intel Core i5-8259U @ 2.3 GHz (4 cores)
4043	
 
Mac Pro (Mid 2012)
Intel Xeon X5675 @ 3.1 GHz (12 cores)
3945	
 
MacBook Pro (13-inch Mid 2020)
Intel Core i5-8257U @ 1.4 GHz (4 cores)
3940	
 
MacBook Pro (13-inch Mid 2019)
Intel Core i5-8257U @ 1.4 GHz (4 cores)
3937	
 
MacBook Pro (15-inch Retina Mid 2015)
Intel Core i7-4980HQ @ 2.8 GHz (4 cores)
3823	
 
MacBook Pro (15-inch Retina Mid 2015)
Intel Core i7-4980HQ @ 2.8 GHz (4 cores)
3823	
 
iMac (21.5-inch Late 2013)
Intel Core i7-4770S @ 3.1 GHz (4 cores)
3799	
 
iMac (27-inch Late 2013)
Intel Core i7-4771 @ 3.5 GHz (4 cores)
3798	
 
Mac Pro (Mid 2010)
Intel Xeon X5670 @ 2.9 GHz (12 cores)
3784	
 
MacBook Pro (15-inch Mid 2017)
Intel Core i7-7920HQ @ 3.1 GHz (4 cores)
3784	
 
iMac (27-inch Retina Mid 2017)
Intel Core i5-7600K @ 3.8 GHz (4 cores)
3748	
 
MacBook Pro (15-inch Mid 2017)
Intel Core i7-7820HQ @ 2.9 GHz (4 cores)
3739	
 
iMac (27-inch Retina Mid 2017)
Intel Core i5-7600 @ 3.5 GHz (4 cores)
3694	
 
MacBook Pro (15-inch Retina Mid 2014)
Intel Core i7-4980HQ @ 2.8 GHz (4 cores)
3653	
 
MacBook Pro (15-inch Late 2016)
Intel Core i7-6920HQ @ 2.9 GHz (4 cores)
3650	
 
MacBook Pro (15-inch Retina Late 2013)
Intel Core i7-4960HQ @ 2.6 GHz (4 cores)
3632	
 
MacBook Pro (15-inch Retina Mid 2015)
Intel Core i7-4870HQ @ 2.5 GHz (4 cores)
3629	
 
MacBook Pro (15-inch Retina Mid 2015)
Intel Core i7-4870HQ @ 2.5 GHz (4 cores)
3629	
 
MacBook Pro (15-inch Mid 2017)
Intel Core i7-7700HQ @ 2.8 GHz (4 cores)
3625	
 
Mac Pro (Late 2013)
Intel Xeon E5-1650 v2 @ 3.5 GHz (6 cores)
3562	
 
MacBook Pro (15-inch Late 2016)
Intel Core i7-6820HQ @ 2.7 GHz (4 cores)
3555	
 
Mac Pro (Mid 2010)
Intel Xeon X5650 @ 2.7 GHz (12 cores)
3539	
 
Mac mini (Late 2018)
Intel Core i3-8100B @ 3.6 GHz (4 cores)
3518	
 
MacBook Pro (15-inch Retina Mid 2014)
Intel Core i7-4870HQ @ 2.5 GHz (4 cores)
3502	
 
iMac (27-inch Retina Late 2015)
Intel Core i5-6600 @ 3.3 GHz (4 cores)
3480	
 
iMac (21.5-inch Retina Mid 2017)
Intel Core i5-7500 @ 3.4 GHz (4 cores)
3472	
 
MacBook Pro (15-inch Retina Mid 2015)
Intel Core i7-4770HQ @ 2.2 GHz (4 cores)
3451	
 
iMac (27-inch Retina Mid 2017)
Intel Core i5-7500 @ 3.4 GHz (4 cores)
3447	
 
MacBook Pro (15-inch Late 2016)
Intel Core i7-6700HQ @ 2.6 GHz (4 cores)
3442	
 
iMac (21.5-inch Retina Early 2019)
Intel Core i3-8100 @ 3.6 GHz (4 cores)
3438	
 
MacBook Pro (15-inch Retina Late 2013)
Intel Core i7-4850HQ @ 2.3 GHz (4 cores)
3429	
 
iMac (21.5-inch Retina Late 2015)
Intel Core i5-5675R @ 3.1 GHz (4 cores)
3411	
 
MacBook Pro (15-inch Retina Mid 2014)
Intel Core i7-4770HQ @ 2.2 GHz (4 cores)
3381	
 
iMac (21.5-inch Retina Mid 2017)
Intel Core i5-7400 @ 3.0 GHz (4 cores)
3274	
 
iMac (27-inch Retina Late 2015)
Intel Core i5-6500 @ 3.2 GHz (4 cores)
3252	
 
Mac Pro (Mid 2012)
Intel Xeon E5645 @ 2.4 GHz (12 cores)
3189	
 
iMac (21.5-inch Late 2015)
Intel Core i5-5575R @ 2.8 GHz (4 cores)
3154	
 
iMac (27-inch Late 2013)
Intel Core i5-4670 @ 3.4 GHz (4 cores)
3142	
 
iMac (27-inch Retina)
Intel Core i5-4690 @ 3.5 GHz (4 cores)
3131	
 
MacBook Pro (15-inch Retina Late 2013)
Intel Core i7-4750HQ @ 2.0 GHz (4 cores)
3127	
 
MacBook Air (Early 2020)
Intel Core i7-1060NG7 @ 1.2 GHz (4 cores)
3090	
 
iMac (27-inch Late 2013)
Intel Core i5-4570 @ 3.2 GHz (4 cores)
2938	
 
iMac (21.5-inch Late 2013)
Intel Core i5-4570S @ 2.9 GHz (4 cores)
2927	
 
iMac (21.5-inch Late 2013)
Intel Core i5-4570R @ 2.7 GHz (4 cores)
2879	
 
MacBook Air (Early 2020)
Intel Core i5-1030NG7 @ 1.1 GHz (4 cores)
2850	
 
Mac Pro (Early 2009)
Intel Xeon X5550 @ 2.7 GHz (8 cores)
2708	
 
Mac Pro (Late 2013)
Intel Xeon E5-1620 v2 @ 3.7 GHz (4 cores)
2621	
 
Mac Pro (Mid 2010)
Intel Xeon W3680 @ 3.3 GHz (6 cores)
2593	
 
iMac (27-inch Late 2012)
Intel Core i7-3770 @ 3.4 GHz (4 cores)
2584	
 
iMac (21.5-inch Late 2012)
Intel Core i7-3770S @ 3.1 GHz (4 cores)
2567	
 
Mac Pro (Mid 2010)
Intel Xeon E5620 @ 2.4 GHz (8 cores)
2521	
 
iMac (21.5-inch Mid 2017)
Intel Core i5-7360U @ 2.3 GHz (2 cores)
2429	
 
MacBook Pro (13-inch Mid 2017)
Intel Core i7-7567U @ 3.5 GHz (2 cores)
2369	
 
Mac mini (Late 2012)
Intel Core i7-3720QM @ 2.6 GHz (4 cores)
2329	
 
MacBook Pro (15-inch Mid 2012)
Intel Core i7-3820QM @ 2.7 GHz (4 cores)
2326	
 
MacBook Pro (15-inch Mid 2012)
Intel Core i7-3720QM @ 2.6 GHz (4 cores)
2308	
 
MacBook Pro (13-inch Mid 2017)
Intel Core i5-7360U @ 2.3 GHz (2 cores)
2282	
 
MacBook Pro (Retina)
Intel Core i7-3820QM @ 2.7 GHz (4 cores)
2278	
 
MacBook Pro (Retina)
Intel Core i7-3720QM @ 2.6 GHz (4 cores)
2266	
 
iMac (27-inch Mid 2011)
Intel Core i7-2600 @ 3.4 GHz (4 cores)
2263	
 
Mac Pro (Early 2009)
Intel Xeon E5520 @ 2.3 GHz (8 cores)
2259	
 
MacBook Pro (15-inch Retina Early 2013)
Intel Core i7-3740QM @ 2.7 GHz (4 cores)
2186	
 
MacBook Pro (15-inch Retina Early 2013)
Intel Core i7-3840QM @ 2.8 GHz (4 cores)
2178	
 
MacBook Pro (13-inch Mid 2017)
Intel Core i5-7267U @ 3.1 GHz (2 cores)
2177	
 
MacBook Pro (15-inch Retina Early 2013)
Intel Core i7-3635QM @ 2.4 GHz (4 cores)
2167	
 
Mac mini (Late 2012)
Intel Core i7-3615QM @ 2.3 GHz (4 cores)
2153	
 
MacBook Pro (13-inch Late 2016)
Intel Core i7-6567U @ 3.3 GHz (2 cores)
2151	
 
MacBook Pro (13-inch Late 2016)
Intel Core i7-6660U @ 2.4 GHz (2 cores)
2118	
 
MacBook Pro (15-inch Mid 2012)
Intel Core i7-3615QM @ 2.3 GHz (4 cores)
2094	
 
MacBook Pro (13-inch Late 2016)
Intel Core i5-6287U @ 3.1 GHz (2 cores)
2087	
 
iMac (27-inch Late 2012)
Intel Core i5-3470 @ 3.2 GHz (4 cores)
2065	
 
MacBook Pro (Retina)
Intel Core i7-3615QM @ 2.3 GHz (4 cores)
2032	
 
MacBook Pro (17-inch Late 2011)
Intel Core i7-2860QM @ 2.5 GHz (4 cores)
2019	
 
iMac (21.5-inch Mid 2011)
Intel Core i7-2600S @ 2.8 GHz (4 cores)
2009	
 
iMac (21.5-inch Late 2012)
Intel Core i5-3470S @ 2.9 GHz (4 cores)
2007	
 
MacBook Pro (13-inch Late 2016)
Intel Core i5-6267U @ 2.9 GHz (2 cores)
2003	
 
MacBook Pro (15-inch Late 2011)
Intel Core i7-2860QM @ 2.5 GHz (4 cores)
1988	
 
iMac (27-inch Late 2012)
Intel Core i5-3470S @ 2.9 GHz (4 cores)
1966	
 
MacBook Pro (13-inch Retina Early 2015)
Intel Core i7-5557U @ 3.1 GHz (2 cores)
1961	
 
MacBook Air (11-inch Early 2015)
Intel Core i7-5650U @ 2.2 GHz (2 cores)
1957	
 
MacBook Pro (17-inch Late 2011)
Intel Core i7-2760QM @ 2.4 GHz (4 cores)
1950	
 
MacBook Pro (15-inch Late 2011)
Intel Core i7-2760QM @ 2.4 GHz (4 cores)
1941	
 
MacBook Pro (13-inch Retina Early 2015)
Intel Core i5-5287U @ 2.9 GHz (2 cores)
1916	
 
Mac mini (Late 2014)
Intel Core i7-4578U @ 3.0 GHz (2 cores)
1900	
 
MacBook Pro (13-inch Late 2016)
Intel Core i5-6360U @ 2.0 GHz (2 cores)
1895	
 
Mac Pro (Early 2008)
Intel Xeon X5482 @ 3.2 GHz (8 cores)
1879	
 
MacBook Air (Early 2020)
Intel Core i3-1000NG4 @ 1.1 GHz (2 cores)
1874	
 
Mac mini (Late 2014)
Intel Core i5-4308U @ 2.8 GHz (2 cores)
1856	
 
MacBook Air (13-inch Early 2015)
Intel Core i7-5650U @ 2.2 GHz (2 cores)
1853	
 
Mac Pro (Early 2008)
Intel Xeon E5472 @ 3.0 GHz (8 cores)
1841	
 
MacBook Pro (13-inch Retina Late 2013)
Intel Core i7-4558U @ 2.8 GHz (2 cores)
1834	
 
MacBook Pro (13-inch Retina Early 2015)
Intel Core i5-5257U @ 2.7 GHz (2 cores)
1825	
 
MacBook Pro (13-inch Retina Mid 2014)
Intel Core i5-4308U @ 2.8 GHz (2 cores)
1823	
 
MacBook Pro (13-inch Retina Mid 2014)
Intel Core i7-4578U @ 3.0 GHz (2 cores)
1819	
 
Mac Pro (Early 2008)
Intel Xeon X5472 @ 3.0 GHz (8 cores)
1792	
 
MacBook Air (11-inch Mid 2013)
Intel Core i7-4650U @ 1.7 GHz (2 cores)
1757	
 
Mac mini (Late 2014)
Intel Core i5-4278U @ 2.6 GHz (2 cores)
1744	
 
MacBook Pro (15-inch Early 2011)
Intel Core i7-2820QM @ 2.3 GHz (4 cores)
1743	
 
MacBook Pro (17-inch Early 2011)
Intel Core i7-2720QM @ 2.2 GHz (4 cores)
1717	
 
iMac (27-inch Mid 2011)
Intel Core i5-2400 @ 3.1 GHz (4 cores)
1713	
 
MacBook (Mid 2017)
Intel Core i7-7Y75 @ 1.4 GHz (2 cores)
1712	
 
MacBook (Mid 2017)
Intel Core i5-7Y54 @ 1.3 GHz (2 cores)
1704	
 
MacBook Pro (15-inch Late 2011)
Intel Core i7-2675QM @ 2.2 GHz (4 cores)
1704	
 
Mac Pro (Mid 2010)
Intel Xeon W3565 @ 3.2 GHz (4 cores)
1698	
 
MacBook Pro (13-inch Retina Mid 2014)
Intel Core i5-4278U @ 2.6 GHz (2 cores)
1691	
 
MacBook Air (13-inch Mid 2013)
Intel Core i7-4650U @ 1.7 GHz (2 cores)
1690	
 
iMac (21.5-inch Late 2012)
Intel Core i5-3335S @ 2.7 GHz (4 cores)
1689	
 
MacBook Pro (13-inch Retina Late 2013)
Intel Core i5-4288U @ 2.6 GHz (2 cores)
1686	
 
MacBook Pro (15-inch Early 2011)
Intel Core i7-2720QM @ 2.2 GHz (4 cores)
1674	
 
iMac (21.5-inch Mid 2011)
Intel Core i5-2500S @ 2.7 GHz (4 cores)
1660	
 
MacBook Air (Late 2018)
Intel Core i5-8210Y @ 1.6 GHz (2 cores)
1645	
 
Mac Pro (Early 2008)
Intel Xeon E5462 @ 2.8 GHz (8 cores)
1630	
 
MacBook (Mid 2017)
Intel Core m3-7Y32 @ 1.2 GHz (2 cores)
1627	
 
iMac (27-inch Mid 2010)
Intel Core i7-870 @ 2.9 GHz (4 cores)
1626	
 
MacBook Air (Mid 2017)
Intel Core i5-5350U @ 1.8 GHz (2 cores)
1612	
 
iMac (27-inch Mid 2011)
Intel Core i5-2500S @ 2.7 GHz (4 cores)
1603	
 
MacBook Pro (13-inch Retina Late 2013)
Intel Core i5-4258U @ 2.4 GHz (2 cores)
1584	
 
iMac (21.5-inch Late 2015)
Intel Core i5-5250U @ 1.6 GHz (2 cores)
1571	
 
Mac Pro (Mid 2010)
Intel Xeon W3530 @ 2.8 GHz (4 cores)
1550	
 
MacBook (Early 2016)
Intel Core m5-6Y54 @ 1.2 GHz (2 cores)
1543	
 
iMac (21.5-inch Mid 2011)
Intel Core i5-2400S @ 2.5 GHz (4 cores)
1528	
 
MacBook (Early 2016)
Intel Core m7-6Y75 @ 1.3 GHz (2 cores)
1528	
 
iMac (27-inch Late 2009)
Intel Core i7-860 @ 2.8 GHz (4 cores)
1516	
 
MacBook Air (13-inch Early 2015)
Intel Core i5-5250U @ 1.6 GHz (2 cores)
1497	
 
MacBook Air (11-inch Early 2015)
Intel Core i5-5250U @ 1.6 GHz (2 cores)
1487	
 
Mac mini (Mid 2011)
Intel Core i7-2635QM @ 2.0 GHz (4 cores)
1478	
 
Mac Pro (Early 2009)
Intel Xeon W3520 @ 2.7 GHz (4 cores)
1466	
 
MacBook Pro (15-inch Early 2011)
Intel Core i7-2635QM @ 2.0 GHz (4 cores)
1420	
 
iMac (21.5-inch Mid 2014)
Intel Core i5-4260U @ 1.4 GHz (2 cores)
1414	
 
Mac mini (Late 2014)
Intel Core i5-4260U @ 1.4 GHz (2 cores)
1385	
 
MacBook Air (13-inch Early 2014)
Intel Core i5-4260U @ 1.4 GHz (2 cores)
1376	
 
MacBook Air (11-inch Early 2014)
Intel Core i5-4260U @ 1.4 GHz (2 cores)
1375	
 
MacBook Pro (13-inch Retina)
Intel Core i7-3520M @ 2.9 GHz (2 cores)
1364	
 
MacBook Air (11-inch Mid 2013)
Intel Core i5-4250U @ 1.3 GHz (2 cores)
1358	
 
MacBook Air (13-inch Mid 2013)
Intel Core i5-4250U @ 1.3 GHz (2 cores)
1349	
 
MacBook (Early 2016)
Intel Core m3-6Y30 @ 1.1 GHz (2 cores)
1337	
 
MacBook (Early 2015)
Intel Core M-5Y51 @ 1.2 GHz (2 cores)
1318	
 
MacBook (Early 2015)
Intel Core M-5Y71 @ 1.3 GHz (2 cores)
1277	
 
iMac (27-inch Mid 2010)
Intel Core i5-760 @ 2.8 GHz (4 cores)
1259	
 
MacBook Pro (13-inch Mid 2012)
Intel Core i7-3520M @ 2.9 GHz (2 cores)
1245	
 
MacBook Pro (13-inch Retina Early 2013)
Intel Core i7-3540M @ 3.0 GHz (2 cores)
1245	
 
MacBook (Early 2015)
Intel Core M-5Y31 @ 1.1 GHz (2 cores)
1216	
 
Mac mini (Mid 2011)
Intel Core i7-2620M @ 2.7 GHz (2 cores)
1122	
 
MacBook Air (11-inch Mid 2012)
Intel Core i7-3667U @ 2.0 GHz (2 cores)
1117	
 
iMac (21.5 inch Late 2011)
Intel Core i3-2100 @ 3.1 GHz (2 cores)
1107	
 
MacBook Pro (13-inch Mid 2012)
Intel Core i5-3210M @ 2.5 GHz (2 cores)
1099	
 
Mac mini (Late 2012)
Intel Core i5-3210M @ 2.5 GHz (2 cores)
1099	
 
MacBook Pro (13-inch Retina)
Intel Core i5-3210M @ 2.5 GHz (2 cores)
1095	
 
MacBook Air (13-inch Mid 2012)
Intel Core i7-3667U @ 2.0 GHz (2 cores)
1094	
 
Mac mini (Mid 2011)
Intel Core i5-2520M @ 2.5 GHz (2 cores)
1085	
 
MacBook Pro (13-inch Retina Early 2013)
Intel Core i5-3230M @ 2.6 GHz (2 cores)
1080	
 
iMac (27-inch Late 2009)
Intel Core i5-750 @ 2.7 GHz (4 cores)
1050	
 
MacBook Pro (13-inch Late 2011)
Intel Core i7-2640M @ 2.8 GHz (2 cores)
1010	
 
MacBook Pro (13-inch Early 2011)
Intel Core i7-2620M @ 2.7 GHz (2 cores)
998	
 
MacBook Air (13-inch Mid 2012)
Intel Core i5-3427U @ 1.8 GHz (2 cores)
982	
 
Mac mini (Mid 2011)
Intel Core i5-2415M @ 2.3 GHz (2 cores)
966	
 
iMac (21.5-inch Mid 2010)
Intel Core i3-550 @ 3.2 GHz (2 cores)
955	
 
MacBook Air (13-inch Mid 2011)
Intel Core i7-2677M @ 1.8 GHz (2 cores)
943	
 
iMac (21.5-inch Mid 2010)
Intel Core i5-680 @ 3.6 GHz (2 cores)
940	
 
MacBook Pro (13-inch Late 2011)
Intel Core i5-2435M @ 2.4 GHz (2 cores)
930	
 
MacBook Air (11-inch Mid 2012)
Intel Core i5-3317U @ 1.7 GHz (2 cores)
907	
 
Mac Pro (Early 2008)
Intel Xeon E5462 @ 2.8 GHz (4 cores)
896	
 
iMac (27-inch Mid 2010)
Intel Core i3-550 @ 3.2 GHz (2 cores)
895	
 
MacBook Pro (17-inch Early 2010)
Intel Core i7-640M @ 2.8 GHz (2 cores)
889	
 
MacBook Pro (13-inch Early 2011)
Intel Core i5-2415M @ 2.3 GHz (2 cores)
873	
 
MacBook Pro (15-inch Early 2010)
Intel Core i7-620M @ 2.7 GHz (2 cores)
848	
 
iMac (21.5-inch Mid 2010)
Intel Core i3-540 @ 3.1 GHz (2 cores)
845	
 
MacBook Air (11-inch Mid 2011)
Intel Core i7-2677M @ 1.8 GHz (2 cores)
822	
 
MacBook Air (13-inch Mid 2011)
Intel Core i5-2557M @ 1.7 GHz (2 cores)
791	
 
MacBook Pro (15-inch Early 2010)
Intel Core i5-520M @ 2.4 GHz (2 cores)
766	
 
MacBook Pro (17-inch Early 2010)
Intel Core i5-540M @ 2.5 GHz (2 cores)
763	
 
MacBook Pro (15-inch Early 2010)
Intel Core i5-540M @ 2.5 GHz (2 cores)
741	
 
MacBook Air (11-inch Mid 2011)
Intel Core i5-2467M @ 1.6 GHz (2 cores)
701	
 
iMac (Late 2009)
Intel Core 2 Duo E8600 @ 3.3 GHz (2 cores)
684	
 
iMac (Late 2009)
Intel Core 2 Duo E7600 @ 3.1 GHz (2 cores)
580	
 
iMac (Early 2008)
Intel Core 2 Duo E8235 @ 2.8 GHz (2 cores)
567	
 
iMac (Early 2009)
Intel Core 2 Duo E8335 @ 2.9 GHz (2 cores)
547	
 
MacBook Pro (15-inch Mid 2009)
Intel Core 2 Duo T9600 @ 2.8 GHz (2 cores)
545	
 
MacBook Pro (17-inch Mid 2009)
Intel Core 2 Duo T9600 @ 2.8 GHz (2 cores)
542	
 
iMac (Early 2009)
Intel Core 2 Duo E8135 @ 2.7 GHz (2 cores)
536	
 
MacBook Pro (Late 2008)
Intel Core 2 Duo T9400 @ 2.5 GHz (2 cores)
536	
 
Mac mini (Late 2009)
Intel Core 2 Duo P8800 @ 2.7 GHz (2 cores)
525	
 
MacBook Pro (17-inch Mid 2009)
Intel Core 2 Duo T9900 @ 3.1 GHz (2 cores)
517	
 
MacBook Pro (15-inch Mid 2009)
Intel Core 2 Duo P8800 @ 2.7 GHz (2 cores)
511	
 
Mac mini (Early 2010)
Intel Core 2 Duo P8800 @ 2.7 GHz (2 cores)
503	
 
Mac mini (Late 2009)
Intel Core 2 Duo P8700 @ 2.5 GHz (2 cores)
503	
 
MacBook Pro (Late 2008)
Intel Core 2 Duo T9550 @ 2.7 GHz (2 cores)
497	
 
MacBook Pro (17-inch Early 2009)
Intel Core 2 Duo T9550 @ 2.7 GHz (2 cores)
481	
 
MacBook Pro (Early 2008)
Intel Core 2 Duo T9300 @ 2.5 GHz (2 cores)
480	
 
MacBook (Mid 2010)
Intel Core 2 Duo P8600 @ 2.4 GHz (2 cores)
476	
 
MacBook Pro (Early 2008)
Intel Core 2 Duo T9500 @ 2.6 GHz (2 cores)
466	
 
MacBook Pro (Early 2008)
Intel Core 2 Duo T8300 @ 2.4 GHz (2 cores)
465	
 
MacBook Pro (13-inch Mid 2009)
Intel Core 2 Duo P8700 @ 2.5 GHz (2 cores)
464	
 
MacBook Pro (13-inch Early 2010)
Intel Core 2 Duo P8600 @ 2.4 GHz (2 cores)
464	
 
MacBook Pro (15-inch Mid 2009)
Intel Core 2 Duo P8700 @ 2.5 GHz (2 cores)
463	
 
MacBook Pro (Late 2008)
Intel Core 2 Duo P8600 @ 2.4 GHz (2 cores)
456	
 
MacBook Pro (13-inch Mid 2009)
Intel Core 2 Duo P7550 @ 2.3 GHz (2 cores)
454	
 
MacBook Pro (13-inch Early 2010)
Intel Core 2 Duo P8800 @ 2.7 GHz (2 cores)
445	
 
MacBook (Late 2008)
Intel Core 2 Duo P8600 @ 2.4 GHz (2 cores)
433	
 
Mac mini (Late 2009)
Intel Core 2 Duo P7550 @ 2.3 GHz (2 cores)
432	
 
MacBook (Late 2009)
Intel Core 2 Duo P7550 @ 2.3 GHz (2 cores)
425	
 
Mac mini (Early 2009)
Intel Core 2 Duo P7350 @ 2.0 GHz (2 cores)
409	
 
MacBook (Late 2008)
Intel Core 2 Duo P7350 @ 2.0 GHz (2 cores)
386	
 
Mac mini (Early 2010)
Intel Core 2 Duo P8600 @ 2.4 GHz (2 cores)
367	
 
MacBook Air (11-inch Late 2010)
Intel Core 2 Duo U9600 @ 1.6 GHz (2 cores)
324	
 
MacBook (Early 2009)
Intel Core 2 Duo P7450 @ 2.1 GHz (2 cores)
274	
 

"""

# Process the raw data

import re


# Function to process the raw data
def process_raw_data(raw_data):
    lines = raw_data.strip().split('\n')
    data = []
    current_entry = []
    
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue
        
        current_entry.append(stripped_line)
        
        if len(current_entry) == 3:
            device = current_entry[0]
            processor = current_entry[1]
            try:
                performance_metric = int(current_entry[2])
            except ValueError:
                performance_metric = None
            
            year_match = re.search(r'\b(20\d{2})\b', device)
            if year_match:
                year = int(year_match.group(1))
            else:
                year = None
            if year and performance_metric:
                data.append((device, processor, performance_metric, year))
            current_entry = []
    
    return data

# Assuming raw_data contains the input data as a string
data = process_raw_data(raw_data)

# Extract years, performance metrics, and processors
years = [int(re.search(r'\d{4}', item[0]).group()) for item in data]
performance_metrics = [item[2] for item in data]
processors = [item[1] for item in data]

# Find the unique years
unique_years = sorted(set(years))

# Create the plot
sns.set(style="whitegrid")

# Create the plot
plt.figure(figsize=(12, 8))

# Create a color palette
palette = sns.color_palette("viridis", as_cmap=True)

# Plot each data point with color gradient based on performance metrics
sc = plt.scatter(years, performance_metrics, c=performance_metrics, cmap=palette, s=100, edgecolor='k', alpha=0.7)

# Draw vertical lines for each year
for year in unique_years:
    yearly_metrics = [performance_metrics[i] for i in range(len(data)) if years[i] == year]
    plt.plot([year, year], [min(yearly_metrics), max(yearly_metrics)], 'k-', linewidth=1)

# Add hover functionality
cursor = mplcursors.cursor(sc, hover=True)
@cursor.connect("add")
def on_add(sel):
    idx = sel.index
    sel.annotation.set(text=processors[idx])

# Set x-ticks to unique years only
plt.xticks(unique_years, fontsize=12)
plt.yticks(fontsize=12)

# Labeling the axes
plt.xlabel('Year', fontsize=14)
#plt.ylabel('Performance Metric', fontsize=14)
plt.title('Performance Metrics of Apple Mac Devices Over the Years', fontsize=16)

# Add a color bar
cbar = plt.colorbar(sc)
cbar.set_label('GeekBench Multithreadedscore', fontsize=14)

# Display the plot
plt.show()
