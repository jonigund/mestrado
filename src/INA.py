import ex003

fator_n = 1
leitura_temperatura = ex003.sensorTempAgua
leitura_ph =  ex003.pHAgua

print("Temperatura: ", leitura_temperatura, " C")
print("pH:          ", leitura_ph)

resultado_temp_inferior = 0
resultado_temp_superior = 0
f37 = resultado_temp_superior
b36 = leitura_ph
b37 = leitura_temperatura
a4 = 6.00
a5 = 8.00
a6 = 10.00
a7 = 12.00
a8 = 14.00
a9 = 16.00
a10 = 18.00
a11 = 20.00
a12 = 22.00
a13 = 24.00
a14 = 26.00
a15 = 28.00
a16 = 30.00
a17 = 32.00
b4 = 0.001300
b5 = 0.001600
b6 = 0.001800
b7 = 0.002200
b8 = 0.002500
b9 = 0.002900
b10 = 0.003400
b11 = 0.003900
b12 = 0.004600
b13 = 0.005200
b14 = 0.006000
b15 = 0.006900
b16 = 0.008000
b17 = 0.009300
q4 = 0.5745
q5 = 0.6131
q6 = 0.6498
q7 = 0.6844
q8 = 0.7166
q9 = 0.7463
q10 = 0.7735
q11	= 0.7983
q12	= 0.8207
q13 = 0.8408
q14 = 0.8588
q15 = 0.8749
q16 = 0.8892
q17 = 0.9058

# coluna de valores pH

b3 = 7
c3 = 7.2
d3 = 7.4
e3 = 7.6
f3 = 7.8
g3 = 8
h3 = 8.2
i3 = 8.4
j3 = 8.6
k3 = 8.8
l3 = 9
m3 = 9.2
n3 = 9.4
o3 = 9.6
p3 = 9.8
q3 = 10


def guide_line(b37, a17, a16, a15, a14, a13, a12, a11, a10, a9, a8, a7, a6, a5, a4):
    if b37 > a17:
        return 17
    elif b37 >= a16:
        return 16
    elif b37 >= a15:
        return 15
    elif b37 >= a14:
        return 14
    elif b37 >= a13:
        return 13
    elif b37 >= a12:
        return 12
    elif b37 >= a11:
        return 11
    elif b37 >= a10:
        return 10
    elif b37 >= a9:
        return 9
    elif b37 >= a8:
        return 8
    elif b37 >= a7:
        return 7
    elif b37 >= a6:
        return 6
    elif b37 >= a5:
        return 5
    elif b37 >= a4:
        return 4
    else:
        return 0


resultado_guide_line = guide_line(b37, a17, a16, a15, a14, a13, a12, a11, a10, a9, a8, a7, a6, a5, a4)
g36 = resultado_guide_line


def calcular_temperatura_superior(b37, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17):
    if b37 > a17:
        return "Temperatura acima do range tabelado"
    elif b37 >= a16:
        return round(q16 + ((b37 - a16) * (q17 - q16) / (a17 - a16)), 6)
    elif b37 >= a15:
        return round(q15 + ((b37 - a15) * (q16 - q15) / (a16 - a15)), 6)
    elif b37 >= a14:
        return round(q14 + ((b37 - a14) * (q15 - q14) / (a15 - a14)), 6)
    elif b37 >= a13:
        return round(q13 + ((b37 - a13) * (q14 - q13) / (a14 - a13)), 6)
    elif b37 >= a12:
        return round(q12 + ((b37 - a12) * (q13 - q12) / (a13 - a12)), 6)
    elif b37 >= a11:
        return round(q11 + ((b37 - a11) * (q12 - q11) / (a12 - a11)), 6)
    elif b37 >= a10:
        return round(q10 + ((b37 - a10) * (q11 - q10) / (a11 - a10)), 6)
    elif b37 >= a9:
        return round(q9 + ((b37 - a9) * (q10 - q9) / (a10 - a9)), 6)
    elif b37 >= a8:
        return round(q8 + ((b37 - a8) * (q9 - q8) / (a9 - a8)), 6)
    elif b37 >= 7:
        return round(q7 + ((b37 - a7) * (q8 - q7) / (a8 - a7)), 6)
    elif b37 >= a6:
        return round(q6 + ((b37 - a6) * (q7 - q6) / (a7 - a6)), 6)
    elif b37 >= a5:
        return round(q5 + ((b37 - a5) * (q6 - q5) / (a6 - a5)), 6)
    elif b37 >= a4:
        return round(q4 + ((b37 - a4) * (q5 - q4) / (a5 - a4)), 6)
    else:
        return "Temperatura abaixo do range tabelado"


resultado_temp_superior = calcular_temperatura_superior(b37, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17)


def calcula_temperatura_inferior(B37, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, B4, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17):
    if B37 > A17:
        return "Temperatura acima do range tabelado"
    elif B37 >= A16:
        return B16 + ((B37 - A16) * (B17 - B16) / (A17 - A16))
    elif B37 >= A15:
        return B15 + ((B37 - A15) * (B16 - B15) / (A16 - A15))
    elif B37 >= A14:
        return B14 + ((B37 - A14) * (B15 - B14) / (A15 - A14))
    elif B37 >= A13:
        return B13 + ((B37 - A13) * (B14 - B13) / (A14 - A13))
    elif B37 >= A12:
        return B12 + ((B37 - A12) * (B13 - B12) / (A13 - A12))
    elif B37 >= A11:
        return B11 + ((B37 - A11) * (B12 - B11) / (A12 - A11))
    elif B37 >= A10:
        return B10 + ((B37 - A10) * (B11 - B10) / (A11 - A10))
    elif B37 >= A9:
        return B9 + ((B37 - A9) * (B10 - B9) / (A10 - A9))
    elif B37 >= A8:
        return B8 + ((B37 - A8) * (B9 - B8) / (A9 - A8))
    elif B37 >= 7:
        return B7 + ((B37 - A7) * (B8 - B7) / (A8 - A7))
    elif B37 >= A6:
        return B6 + ((B37 - A6) * (B7 - B6) / (A7 - A6))
    elif B37 >= A5:
        return B5 + ((B37 - A5) * (B6 - B5) / (A6 - A5))
    elif B37 >= A4:
        return B4 + ((B37 - A4) * (B5 - B4) / (A5 - A4))
    else:
        return "Temperatura abaixo do range tabelado"


resultado_temp_inferior = calcula_temperatura_inferior(b37, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17)


# Bloco de variaveis de ajuste guide line
ajuste_min_4 = 0
ajuste_max_4 = 0
ajuste_min_5 = 0
ajuste_max_5 = 0
ajuste_min_6 = 0
ajuste_max_6 = 0
ajuste_min_7 = 0
ajuste_max_7 = 0
ajuste_min_8 = 0
ajuste_max_8 = 0
ajuste_min_9 = 0
ajuste_max_9 = 0
ajuste_min_10 = 0
ajuste_max_10 = 0
ajuste_min_11 = 0
ajuste_max_11 = 0
ajuste_min_12 = 0
ajuste_max_12 = 0
ajuste_min_13 = 0
ajuste_max_13 = 0
ajuste_min_14 = 0
ajuste_max_14 = 0
ajuste_min_15 = 0
ajuste_max_15 = 0
ajuste_min_16 = 0
ajuste_max_16 = 0
ajuste_min_17 = 0
ajuste_max_17 = 0


# Bloco BOYD corrigido
b19	 =	0.00226283724978242
b20	 =	0.00260968846843908
b21	 =	0.00277008310249307
b22	 =	0.00321449444769141
b23	 =	0.00348869662294167
b24	 =	0.00388583679485462
b25	 =	0.0043956043956044
b26	 =	0.00488538143555055
b27	 =	0.00560497136590715
b28	 =	0.00618458610846813
b29	 =	0.00698649278062413
b30	 =	0.00788661561321294
b31	 =	0.00899685110211426
b32	 =	0.0102671671450651

c19	 =	0.00365535248041775
c20	 =	0.00407763823193606
c21	 =	0.00446291166512773
c22	 =	0.00496785505552309
c23	 =	0.00558191459670667
c24	 =	0.00616374112287284
c25	 =	0.00698125404007757
c26	 =	0.00776650382061881
c27	 =	0.00877299865968076
c28	 =	0.00987155090390105
c29	 =	0.0111783884489986
c30	 =	0.0125728654703395
c31	 =	0.01417004048583
c32	 =	0.0165599470081696

d19	 =	0.00591818973020017
d20	 =	0.0065242211710977
d21	 =	0.00707910126192675
d22	 =	0.00789012273524255
d23	 =	0.00879151548981301
d24	 =	0.00978158917325472
d25	 =	0.010989010989011
d26	 =	0.0122760866842039
d27	 =	0.0138905812111612
d28	 =	0.0155803996194101
d29	 =	0.0174662319515603
d30	 =	0.0197736884215339
d31	 =	0.0222672064777328
d32	 =	0.0260543166261868

e19	 =	0.0092254134029591
e20	 =	0.0102756483444789
e21	 =	0.0112342259156664
e22	 =	0.0125657510227937
e23	 =	0.0139547864917667
e24	 =	0.0155433471794185
e25	 =	0.0173238526179703
e26	 =	0.019416259551547
e27	 =	0.0218106494455952
e28	 =	0.024500475737393
e29	 =	0.0274802049371216
e30	 =	0.0309749685678363
e31	 =	0.0348627980206928
e32	 =	0.0407374696400972

f19	 =	0.014621409921671
f20	 =	0.0161474473984668
f21	 =	0.0178516466605109
f22	 =	0.0197253068381064
f23	 =	0.0219090147920737
f24	 =	0.0243869757470186
f25	 =	0.027278603749192
f26	 =	0.0305649505198547
f27	 =	0.0342390642134763
f28	 =	0.0382968601332065
f29	 =	0.0430833721471821
f30	 =	0.0483483826723054
f31	 =	0.0542060278902384
f32	 =	0.0631485979244866

g19	 =	0.0231505657093124
g20	 =	0.025444462567281
g21	 =	0.0280086180363189
g22	 =	0.0309760374050263
g23	 =	0.0344683226346637
g24	 =	0.0383223904596007
g25	 =	0.0426632191338074
g26	 =	0.0477264186396092
g27	 =	0.0533690751797246
g28	 =	0.0597050428163654
g29	 =	0.0668374476013041
g30	 =	0.0747514001600183
g31	 =	0.0835582546108862
g32	 =	0.0968204901744314

h19	 =	0.0365535248041775
h20	 =	0.0399608546729734
h21	 =	0.0440135426285011
h22	 =	0.0485096434833431
h23	 =	0.0537259279933017
h24	 =	0.0596274956451829
h25	 =	0.0664511958629606
h26	 =	0.0739070524865339
h27	 =	0.0823687096381138
h28	 =	0.0918173168411037
h29	 =	0.102468560782487
h30	 =	0.11407017944908
h31	 =	0.126968061178588
h32	 =	0.145948332965335

i19	 =	0.0570931244560487
i20	 =	0.0624694177132605
i21	 =	0.0684826100338566
i22	 =	0.0755406195207481
i23	 =	0.0833100753558471
i24	 =	0.0921881280986199
i25	 =	0.10213316095669
i26	 =	0.113240636352249
i27	 =	0.125624466918484
i28	 =	0.139272121788773
i29	 =	0.154401490451793
i30	 =	0.170876671619614
i31	 =	0.188708951866847
i32	 =	0.215058511812762

j19	 =	0.0887728459530026
j20	 =	0.0967215788615234
j21	 =	0.105878731917513
j22	 =	0.116160140268849
j23	 =	0.127546748534747
j24	 =	0.140426102103712
j25	 =	0.154751131221719
j26	 =	0.170487285481648
j27	 =	0.18776654075789
j28	 =	0.206588962892483
j29	 =	0.227061015370284
j30	 =	0.248942736312721
j31	 =	0.272379667116509
j32	 =	0.305586222124089

k19	 =	0.136640557006092
k20	 =	0.148262926113195
k21	 =	0.161280393967375
k22	 =	0.175920514319112
k23	 =	0.192017862126709
k24	 =	0.209835186922149
k25	 =	0.229217840982547
k26	 =	0.250281848928974
k27	 =	0.273059583282564
k28	 =	0.297335870599429
k29	 =	0.323008849557522
k30	 =	0.34998285518345
k31	 =	0.378092667566352
k32	 =	0.416869066018989

l19	 =	0.207136640557006
l20	 =	0.223128364051541
l21	 =	0.240843336411203
l22	 =	0.260374050263004
l23	 =	0.281607591403851
l24	 =	0.30456920809326
l25	 =	0.329153199741435
l26	 =	0.355254916697983
l27	 =	0.382600219324966
l28	 =	0.411037107516651
l29	 =	0.440498369818351
l30	 =	0.470453766144702
l31	 =	0.500787224471435
l32	 =	0.541179068226982

m19	 =	0.306875543951262
m20	 =	0.327515902789105
m21	 =	0.349799938442598
m22	 =	0.373758036236119
m23	 =	0.399246441529445
m24	 =	0.426102103711644
m25	 =	0.454040077569489
m26	 =	0.482901164975573
m27	 =	0.512245643962471
m28	 =	0.541983824928639
m29	 =	0.571611551001397
m30	 =	0.600982969482227
m31	 =	0.629667116509222
m32	 =	0.666593066902186

n19	 =	0.440905134899913
n20	 =	0.464361441852879
n21	 =	0.48938134810711
n22	 =	0.515195791934541
n23	 =	0.542003907340218
n24	 =	0.569342087632319
n25	 =	0.597026502908856
n26	 =	0.624451960415884
n27	 =	0.65163884488851
n28	 =	0.678163653663178
n29	 =	0.703889147647881
n30	 =	0.728426105840667
n31	 =	0.751799370220423
n32	 =	0.780746301611835

o19	 =	0.608529155787641
o20	 =	0.630892187245148
o21	 =	0.65389350569406
o22	 =	0.676943308007013
o23	 =	0.699972090427016
o24	 =	0.722765643842959
o25	 =	0.744925662572722
o26	 =	0.766253288237505
o27	 =	0.786645546484708
o28	 =	0.806018078020932
o29	 =	0.824173265020959
o30	 =	0.841010401188707
o31	 =	0.856612685560054
o32	 =	0.875358798851844

p19	 =	0.800696257615318
p20	 =	0.815527646387213
p21	 =	0.830101569713758
p22	 =	0.841320864991233
p23	 =	0.857800725648898
p24	 =	0.870829425164143
p25	 =	0.883128636069813
p26	 =	0.894400601277715
p27	 =	0.905081028390399
p28	 =	0.914843006660323
p29	 =	0.923730787144853
p30	 =	0.931877928906161
p31	 =	0.939158794421952
p32	 =	0.947780967100905

q19	 =	1
q20	 =	1
q21	 =	1
q22	 =	1
q23	 =	1
q24	 =	1
q25	 =	1
q26	 =	1
q27	 =	1
q28	 =	1
q29	 =	1
q30	 =	1
q31	 =	1
q32	 =	1


# Bloco de ajuste min_max
def cal_ajust_min_4(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16, p19, o19, n19, m19, l19, k19, j19, i19, h19, g19, f19, e19, d19, c19, b19):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p19
    elif b36 >= o3:
        return f37 * o19
    elif b36 >= n3:
        return f37 * n19
    elif b36 >= m3:
        return f37 * m19
    elif b36 >= l3:
        return f37 * l19
    elif b36 >= k3:
        return f37 * k19
    elif b36 >= j3:
        return f37 * j19
    elif b36 >= i3:
        return f37 * i19
    elif b36 >= h3:
        return f37 * h19
    elif b36 >= g3:
        return f37 * g19
    elif b36 >= f3:
        return f37 * f19
    elif b36 >= e3:
        return f37 * e19
    elif b36 >= d3:
        return f37 * d19
    elif b36 >= c3:
        return f37 * c19
    elif b36 >= b3:
        return f37 * b19
    else:
        return 0


ajuste_min_4 =  cal_ajust_min_4(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16, p19, o19, n19, m19, l19, k19, j19, i19, h19, g19, f19, e19, d19, c19, b19)


def cal_ajust_max_4(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3, f37, q19, p19, o19, n19, m19, l19, k19, j19, i19, h19, g19, f19, e19, d19, c19, b19):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q19
    elif b36 >= o3:
        return f37 * p19
    elif b36 >= n3:
        return f37 * o19
    elif b36 >= m3:
        return f37 * n19
    elif b36 >= l3:
        return f37 * m19
    elif b36 >= k3:
        return f37 * l19
    elif b36 >= j3:
        return f37 * k19
    elif b36 >= i3:
        return f37 * j19
    elif b36 >= h3:
        return f37 * i19
    elif b36 >= g3:
        return f37 * h19
    elif b36 >= f3:
        return f37 * g19
    elif b36 >= e3:
        return f37 * f19
    elif b36 >= d3:
        return f37 * e19
    elif b36 >= c3:
        return f37 * d19
    elif b36 >= b3:
        return f37 * c19
    else:
        return 0


ajuste_max_4 = cal_ajust_max_4(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3, f37, q19, p19, o19, n19, m19, l19, k19, j19, i19, h19, g19, f19, e19, d19, c19, b19)


def cal_ajust_min_5(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p20
    elif b36 >= o3:
        return f37 * o20
    elif b36 >= n3:
        return f37 * n20
    elif b36 >= m3:
        return f37 * m20
    elif b36 >= l3:
        return f37 * l20
    elif b36 >= k3:
        return f37 * k20
    elif b36 >= j3:
        return f37 * j20
    elif b36 >= i3:
        return f37 * i20
    elif b36 >= h3:
        return f37 * h20
    elif b36 >= g3:
        return f37 * g20
    elif b36 >= f3:
        return f37 * f20
    elif b36 >= e3:
        return f37 * e20
    elif b36 >= d3:
        return f37 * d20
    elif b36 >= c3:
        return f37 * c20
    elif b36 >= b3:
        return f37 * b20
    else:
        return 0


ajuste_min_5 =  cal_ajust_min_5(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_5(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q20
    elif b36 >= o3:
        return f37 * p20
    elif b36 >= n3:
        return f37 * o20
    elif b36 >= m3:
        return f37 * n20
    elif b36 >= l3:
        return f37 * m20
    elif b36 >= k3:
        return f37 * l20
    elif b36 >= j3:
        return f37 * k20
    elif b36 >= i3:
        return f37 * j20
    elif b36 >= h3:
        return f37 * i20
    elif b36 >= g3:
        return f37 * h20
    elif b36 >= f3:
        return f37 * g20
    elif b36 >= e3:
        return f37 * f20
    elif b36 >= d3:
        return f37 * e20
    elif b36 >= c3:
        return f37 * d20
    elif b36 >= b3:
        return f37 * c20
    else:
        return 0


ajuste_max_5 = cal_ajust_max_5(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_6(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p21
    elif b36 >= o3:
        return f37 * o21
    elif b36 >= n3:
        return f37 * n21
    elif b36 >= m3:
        return f37 * m21
    elif b36 >= l3:
        return f37 * l21
    elif b36 >= k3:
        return f37 * k21
    elif b36 >= j3:
        return f37 * j21
    elif b36 >= i3:
        return f37 * i21
    elif b36 >= h3:
        return f37 * h21
    elif b36 >= g3:
        return f37 * g21
    elif b36 >= f3:
        return f37 * f21
    elif b36 >= e3:
        return f37 * e21
    elif b36 >= d3:
        return f37 * d21
    elif b36 >= c3:
        return f37 * c21
    elif b36 >= b3:
        return f37 * b21
    else:
        return 0


ajuste_min_6 =  cal_ajust_min_6(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_6(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q21
    elif b36 >= o3:
        return f37 * p21
    elif b36 >= n3:
        return f37 * o21
    elif b36 >= m3:
        return f37 * n21
    elif b36 >= l3:
        return f37 * m21
    elif b36 >= k3:
        return f37 * l21
    elif b36 >= j3:
        return f37 * k21
    elif b36 >= i3:
        return f37 * j21
    elif b36 >= h3:
        return f37 * i21
    elif b36 >= g3:
        return f37 * h21
    elif b36 >= f3:
        return f37 * g21
    elif b36 >= e3:
        return f37 * f21
    elif b36 >= d3:
        return f37 * e21
    elif b36 >= c3:
        return f37 * d21
    elif b36 >= b3:
        return f37 * c21
    else:
        return 0


ajuste_max_6 = cal_ajust_max_6(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_7(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p22
    elif b36 >= o3:
        return f37 * o22
    elif b36 >= n3:
        return f37 * n22
    elif b36 >= m3:
        return f37 * m22
    elif b36 >= l3:
        return f37 * l22
    elif b36 >= k3:
        return f37 * k22
    elif b36 >= j3:
        return f37 * j22
    elif b36 >= i3:
        return f37 * i22
    elif b36 >= h3:
        return f37 * h22
    elif b36 >= g3:
        return f37 * g22
    elif b36 >= f3:
        return f37 * f22
    elif b36 >= e3:
        return f37 * e22
    elif b36 >= d3:
        return f37 * d22
    elif b36 >= c3:
        return f37 * c22
    elif b36 >= b3:
        return f37 * b22
    else:
        return 0


ajuste_min_7 =  cal_ajust_min_7(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_7(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q22
    elif b36 >= o3:
        return f37 * p22
    elif b36 >= n3:
        return f37 * o22
    elif b36 >= m3:
        return f37 * n22
    elif b36 >= l3:
        return f37 * m22
    elif b36 >= k3:
        return f37 * l22
    elif b36 >= j3:
        return f37 * k22
    elif b36 >= i3:
        return f37 * j22
    elif b36 >= h3:
        return f37 * i22
    elif b36 >= g3:
        return f37 * h22
    elif b36 >= f3:
        return f37 * g22
    elif b36 >= e3:
        return f37 * f22
    elif b36 >= d3:
        return f37 * e22
    elif b36 >= c3:
        return f37 * d22
    elif b36 >= b3:
        return f37 * c22
    else:
        return 0


ajuste_max_7 = cal_ajust_max_7(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_8(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p23
    elif b36 >= o3:
        return f37 * o23
    elif b36 >= n3:
        return f37 * n23
    elif b36 >= m3:
        return f37 * m23
    elif b36 >= l3:
        return f37 * l23
    elif b36 >= k3:
        return f37 * k23
    elif b36 >= j3:
        return f37 * j23
    elif b36 >= i3:
        return f37 * i23
    elif b36 >= h3:
        return f37 * h23
    elif b36 >= g3:
        return f37 * g23
    elif b36 >= f3:
        return f37 * f23
    elif b36 >= e3:
        return f37 * e23
    elif b36 >= d3:
        return f37 * d23
    elif b36 >= c3:
        return f37 * c23
    elif b36 >= b3:
        return f37 * b23
    else:
        return 0


ajuste_min_8 =  cal_ajust_min_8(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_8(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q23
    elif b36 >= o3:
        return f37 * p23
    elif b36 >= n3:
        return f37 * o23
    elif b36 >= m3:
        return f37 * n23
    elif b36 >= l3:
        return f37 * m23
    elif b36 >= k3:
        return f37 * l23
    elif b36 >= j3:
        return f37 * k23
    elif b36 >= i3:
        return f37 * j23
    elif b36 >= h3:
        return f37 * i23
    elif b36 >= g3:
        return f37 * h23
    elif b36 >= f3:
        return f37 * g23
    elif b36 >= e3:
        return f37 * f23
    elif b36 >= d3:
        return f37 * e23
    elif b36 >= c3:
        return f37 * d23
    elif b36 >= b3:
        return f37 * c23
    else:
        return 0


ajuste_max_8 = cal_ajust_max_8(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_9(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p24
    elif b36 >= o3:
        return f37 * o24
    elif b36 >= n3:
        return f37 * n24
    elif b36 >= m3:
        return f37 * m24
    elif b36 >= l3:
        return f37 * l24
    elif b36 >= k3:
        return f37 * k24
    elif b36 >= j3:
        return f37 * j24
    elif b36 >= i3:
        return f37 * i24
    elif b36 >= h3:
        return f37 * h24
    elif b36 >= g3:
        return f37 * g24
    elif b36 >= f3:
        return f37 * f24
    elif b36 >= e3:
        return f37 * e24
    elif b36 >= d3:
        return f37 * d24
    elif b36 >= c3:
        return f37 * c24
    elif b36 >= b3:
        return f37 * b24
    else:
        return 0


ajuste_min_9 =  cal_ajust_min_9(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_9(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q24
    elif b36 >= o3:
        return f37 * p24
    elif b36 >= n3:
        return f37 * o24
    elif b36 >= m3:
        return f37 * n24
    elif b36 >= l3:
        return f37 * m24
    elif b36 >= k3:
        return f37 * l24
    elif b36 >= j3:
        return f37 * k24
    elif b36 >= i3:
        return f37 * j24
    elif b36 >= h3:
        return f37 * i24
    elif b36 >= g3:
        return f37 * h24
    elif b36 >= f3:
        return f37 * g24
    elif b36 >= e3:
        return f37 * f24
    elif b36 >= d3:
        return f37 * e24
    elif b36 >= c3:
        return f37 * d24
    elif b36 >= b3:
        return f37 * c24
    else:
        return 0


ajuste_max_9 = cal_ajust_max_9(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_10(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p25
    elif b36 >= o3:
        return f37 * o25
    elif b36 >= n3:
        return f37 * n25
    elif b36 >= m3:
        return f37 * m25
    elif b36 >= l3:
        return f37 * l25
    elif b36 >= k3:
        return f37 * k25
    elif b36 >= j3:
        return f37 * j25
    elif b36 >= i3:
        return f37 * i25
    elif b36 >= h3:
        return f37 * h25
    elif b36 >= g3:
        return f37 * g25
    elif b36 >= f3:
        return f37 * f25
    elif b36 >= e3:
        return f37 * e25
    elif b36 >= d3:
        return f37 * d25
    elif b36 >= c3:
        return f37 * c25
    elif b36 >= b3:
        return f37 * b25
    else:
        return 0


ajuste_min_10 =  cal_ajust_min_10(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_10(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q25
    elif b36 >= o3:
        return f37 * p25
    elif b36 >= n3:
        return f37 * o25
    elif b36 >= m3:
        return f37 * n25
    elif b36 >= l3:
        return f37 * m25
    elif b36 >= k3:
        return f37 * l25
    elif b36 >= j3:
        return f37 * k25
    elif b36 >= i3:
        return f37 * j25
    elif b36 >= h3:
        return f37 * i25
    elif b36 >= g3:
        return f37 * h25
    elif b36 >= f3:
        return f37 * g25
    elif b36 >= e3:
        return f37 * f25
    elif b36 >= d3:
        return f37 * e25
    elif b36 >= c3:
        return f37 * d25
    elif b36 >= b3:
        return f37 * c25
    else:
        return 0


ajuste_max_10 = cal_ajust_max_10(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_11(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p26
    elif b36 >= o3:
        return f37 * o26
    elif b36 >= n3:
        return f37 * n26
    elif b36 >= m3:
        return f37 * m26
    elif b36 >= l3:
        return f37 * l26
    elif b36 >= k3:
        return f37 * k26
    elif b36 >= j3:
        return f37 * j26
    elif b36 >= i3:
        return f37 * i26
    elif b36 >= h3:
        return f37 * h26
    elif b36 >= g3:
        return f37 * g26
    elif b36 >= f3:
        return f37 * f26
    elif b36 >= e3:
        return f37 * e26
    elif b36 >= d3:
        return f37 * d26
    elif b36 >= c3:
        return f37 * c26
    elif b36 >= b3:
        return f37 * b26
    else:
        return 0


ajuste_min_11 =  cal_ajust_min_11(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_11(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q26
    elif b36 >= o3:
        return f37 * p26
    elif b36 >= n3:
        return f37 * o26
    elif b36 >= m3:
        return f37 * n26
    elif b36 >= l3:
        return f37 * m26
    elif b36 >= k3:
        return f37 * l26
    elif b36 >= j3:
        return f37 * k26
    elif b36 >= i3:
        return f37 * j26
    elif b36 >= h3:
        return f37 * i26
    elif b36 >= g3:
        return f37 * h26
    elif b36 >= f3:
        return f37 * g26
    elif b36 >= e3:
        return f37 * f26
    elif b36 >= d3:
        return f37 * e26
    elif b36 >= c3:
        return f37 * d26
    elif b36 >= b3:
        return f37 * c26
    else:
        return 0


ajuste_max_11 = cal_ajust_max_11(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_12(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p27
    elif b36 >= o3:
        return f37 * o27
    elif b36 >= n3:
        return f37 * n27
    elif b36 >= m3:
        return f37 * m27
    elif b36 >= l3:
        return f37 * l27
    elif b36 >= k3:
        return f37 * k27
    elif b36 >= j3:
        return f37 * j27
    elif b36 >= i3:
        return f37 * i27
    elif b36 >= h3:
        return f37 * h27
    elif b36 >= g3:
        return f37 * g27
    elif b36 >= f3:
        return f37 * f27
    elif b36 >= e3:
        return f37 * e27
    elif b36 >= d3:
        return f37 * d27
    elif b36 >= c3:
        return f37 * c27
    elif b36 >= b3:
        return f37 * b27
    else:
        return 0


ajuste_min_12 =  cal_ajust_min_12(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_12(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q27
    elif b36 >= o3:
        return f37 * p27
    elif b36 >= n3:
        return f37 * o27
    elif b36 >= m3:
        return f37 * n27
    elif b36 >= l3:
        return f37 * m27
    elif b36 >= k3:
        return f37 * l27
    elif b36 >= j3:
        return f37 * k27
    elif b36 >= i3:
        return f37 * j27
    elif b36 >= h3:
        return f37 * i27
    elif b36 >= g3:
        return f37 * h27
    elif b36 >= f3:
        return f37 * g27
    elif b36 >= e3:
        return f37 * f27
    elif b36 >= d3:
        return f37 * e27
    elif b36 >= c3:
        return f37 * d27
    elif b36 >= b3:
        return f37 * c27
    else:
        return 0

ajuste_max_12 = cal_ajust_max_12(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_13(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p28
    elif b36 >= o3:
        return f37 * o28
    elif b36 >= n3:
        return f37 * n28
    elif b36 >= m3:
        return f37 * m28
    elif b36 >= l3:
        return f37 * l28
    elif b36 >= k3:
        return f37 * k28
    elif b36 >= j3:
        return f37 * j28
    elif b36 >= i3:
        return f37 * i28
    elif b36 >= h3:
        return f37 * h28
    elif b36 >= g3:
        return f37 * g28
    elif b36 >= f3:
        return f37 * f28
    elif b36 >= e3:
        return f37 * e28
    elif b36 >= d3:
        return f37 * d28
    elif b36 >= c3:
        return f37 * c28
    elif b36 >= b3:
        return f37 * b28
    else:
        return 0


ajuste_min_13 =  cal_ajust_min_13(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_13(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q28
    elif b36 >= o3:
        return f37 * p28
    elif b36 >= n3:
        return f37 * o28
    elif b36 >= m3:
        return f37 * n28
    elif b36 >= l3:
        return f37 * m28
    elif b36 >= k3:
        return f37 * l28
    elif b36 >= j3:
        return f37 * k28
    elif b36 >= i3:
        return f37 * j28
    elif b36 >= h3:
        return f37 * i28
    elif b36 >= g3:
        return f37 * h28
    elif b36 >= f3:
        return f37 * g28
    elif b36 >= e3:
        return f37 * f28
    elif b36 >= d3:
        return f37 * e28
    elif b36 >= c3:
        return f37 * d28
    elif b36 >= b3:
        return f37 * c28
    else:
        return 0


ajuste_max_13 = cal_ajust_max_13(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_14(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p29
    elif b36 >= o3:
        return f37 * o29
    elif b36 >= n3:
        return f37 * n29
    elif b36 >= m3:
        return f37 * m29
    elif b36 >= l3:
        return f37 * l29
    elif b36 >= k3:
        return f37 * k29
    elif b36 >= j3:
        return f37 * j29
    elif b36 >= i3:
        return f37 * i29
    elif b36 >= h3:
        return f37 * h29
    elif b36 >= g3:
        return f37 * g29
    elif b36 >= f3:
        return f37 * f29
    elif b36 >= e3:
        return f37 * e29
    elif b36 >= d3:
        return f37 * d29
    elif b36 >= c3:
        return f37 * c29
    elif b36 >= b3:
        return f37 * b29
    else:
        return 0


ajuste_min_14 =  cal_ajust_min_14(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_14(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q29
    elif b36 >= o3:
        return f37 * p29
    elif b36 >= n3:
        return f37 * o29
    elif b36 >= m3:
        return f37 * n29
    elif b36 >= l3:
        return f37 * m29
    elif b36 >= k3:
        return f37 * l29
    elif b36 >= j3:
        return f37 * k29
    elif b36 >= i3:
        return f37 * j29
    elif b36 >= h3:
        return f37 * i29
    elif b36 >= g3:
        return f37 * h29
    elif b36 >= f3:
        return f37 * g29
    elif b36 >= e3:
        return f37 * f29
    elif b36 >= d3:
        return f37 * e29
    elif b36 >= c3:
        return f37 * d29
    elif b36 >= b3:
        return f37 * c29
    else:
        return 0


ajuste_max_14 = cal_ajust_max_14(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_15(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p30
    elif b36 >= o3:
        return f37 * o30
    elif b36 >= n3:
        return f37 * n30
    elif b36 >= m3:
        return f37 * m30
    elif b36 >= l3:
        return f37 * l30
    elif b36 >= k3:
        return f37 * k30
    elif b36 >= j3:
        return f37 * j30
    elif b36 >= i3:
        return f37 * i30
    elif b36 >= h3:
        return f37 * h30
    elif b36 >= g3:
        return f37 * g30
    elif b36 >= f3:
        return f37 * f30
    elif b36 >= e3:
        return f37 * e30
    elif b36 >= d3:
        return f37 * d30
    elif b36 >= c3:
        return f37 * c30
    elif b36 >= b3:
        return f37 * b30
    else:
        return 0


ajuste_min_15 =  cal_ajust_min_15(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_15(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q30
    elif b36 >= o3:
        return f37 * p30
    elif b36 >= n3:
        return f37 * o30
    elif b36 >= m3:
        return f37 * n30
    elif b36 >= l3:
        return f37 * m30
    elif b36 >= k3:
        return f37 * l30
    elif b36 >= j3:
        return f37 * k30
    elif b36 >= i3:
        return f37 * j30
    elif b36 >= h3:
        return f37 * i30
    elif b36 >= g3:
        return f37 * h30
    elif b36 >= f3:
        return f37 * g30
    elif b36 >= e3:
        return f37 * f30
    elif b36 >= d3:
        return f37 * e30
    elif b36 >= c3:
        return f37 * d30
    elif b36 >= b3:
        return f37 * c30
    else:
        return 0


ajuste_max_15 = cal_ajust_max_15(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_16(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p31
    elif b36 >= o3:
        return f37 * o31
    elif b36 >= n3:
        return f37 * n31
    elif b36 >= m3:
        return f37 * m31
    elif b36 >= l3:
        return f37 * l31
    elif b36 >= k3:
        return f37 * k31
    elif b36 >= j3:
        return f37 * j31
    elif b36 >= i3:
        return f37 * i31
    elif b36 >= h3:
        return f37 * h31
    elif b36 >= g3:
        return f37 * g31
    elif b36 >= f3:
        return f37 * f31
    elif b36 >= e3:
        return f37 * e31
    elif b36 >= d3:
        return f37 * d31
    elif b36 >= c3:
        return f37 * c31
    elif b36 >= b3:
        return f37 * b31
    else:
        return 0


ajuste_min_16 =  cal_ajust_min_16(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_16(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q31
    elif b36 >= o3:
        return f37 * p31
    elif b36 >= n3:
        return f37 * o31
    elif b36 >= m3:
        return f37 * n31
    elif b36 >= l3:
        return f37 * m31
    elif b36 >= k3:
        return f37 * l31
    elif b36 >= j3:
        return f37 * k31
    elif b36 >= i3:
        return f37 * j31
    elif b36 >= h3:
        return f37 * i31
    elif b36 >= g3:
        return f37 * h31
    elif b36 >= f3:
        return f37 * g31
    elif b36 >= e3:
        return f37 * f31
    elif b36 >= d3:
        return f37 * e31
    elif b36 >= c3:
        return f37 * d31
    elif b36 >= b3:
        return f37 * c31
    else:
        return 0


ajuste_max_16 = cal_ajust_max_16(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


def cal_ajust_min_17(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16):
    f37 = resultado_temp_superior
    if  b36 >= q3:
        return q16
    elif b36 >= p3:
        return f37 * p32
    elif b36 >= o3:
        return f37 * o32
    elif b36 >= n3:
        return f37 * n32
    elif b36 >= m3:
        return f37 * m32
    elif b36 >= l3:
        return f37 * l32
    elif b36 >= k3:
        return f37 * k32
    elif b36 >= j3:
        return f37 * j32
    elif b36 >= i3:
        return f37 * i32
    elif b36 >= h3:
        return f37 * h32
    elif b36 >= g3:
        return f37 * g32
    elif b36 >= f3:
        return f37 * f32
    elif b36 >= e3:
        return f37 * e32
    elif b36 >= d3:
        return f37 * d32
    elif b36 >= c3:
        return f37 * c32
    elif b36 >= b3:
        return f37 * b32
    else:
        return 0


ajuste_min_17 =  cal_ajust_min_17(b36, f37, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, q16)


def cal_ajust_max_17(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3):
    f37 = resultado_temp_superior
    if b36 >= q3:
        return  1
    elif b36 >= p3:
        return f37 * q32
    elif b36 >= o3:
        return f37 * p32
    elif b36 >= n3:
        return f37 * o32
    elif b36 >= m3:
        return f37 * n32
    elif b36 >= l3:
        return f37 * m32
    elif b36 >= k3:
        return f37 * l32
    elif b36 >= j3:
        return f37 * k32
    elif b36 >= i3:
        return f37 * j32
    elif b36 >= h3:
        return f37 * i32
    elif b36 >= g3:
        return f37 * h32
    elif b36 >= f3:
        return f37 * g32
    elif b36 >= e3:
        return f37 * f32
    elif b36 >= d3:
        return f37 * e32
    elif b36 >= c3:
        return f37 * d32
    elif b36 >= b3:
        return f37 * c32
    else:
        return 0


ajuste_max_17 = cal_ajust_max_17(b36, q3, p3, o3, n3, m3, l3, k3, j3, i3, h3, g3, f3, e3, d3, c3, b3)


# Bloco de max e mim ajustadas

s19	 = ajuste_min_4
s20	 = ajuste_min_5
s21	 =ajuste_min_6
s22	 =ajuste_min_7
s23	 =ajuste_min_8
s24	 =ajuste_min_9
s25	 =ajuste_min_10
s26	 =ajuste_min_11
s27	 =ajuste_min_12
s28	 =ajuste_min_13
s29	 =ajuste_max_14
s30	 =ajuste_min_15
s31	 =ajuste_min_16
s32	 =ajuste_min_17
t19	 =ajuste_max_4
t20	 =ajuste_max_5
t21	 =ajuste_max_6
t22	 =ajuste_max_7
t23	 =ajuste_max_8
t24	 =ajuste_max_9
t25	 =ajuste_max_10
t26	 =ajuste_max_11
t27	 =ajuste_max_12
t28	 =ajuste_max_13
t29	 =ajuste_max_14
t30	 =ajuste_max_15
t31	 =ajuste_max_16
t32	 =ajuste_max_17


def calc_minimo_ajustado(g36, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32):
    if g36 == 0:
        return 0
    elif g36 == 4:
        return s19
    elif g36 == 5:
        return s20
    elif g36 == 6:
        return s21
    elif g36 == 7:
        return s22
    elif g36 == 8:
        return s23
    elif g36 == 9:
        return s24
    elif g36 == 10:
        return s25
    elif g36 == 11:
        return s26
    elif g36 == 12:
        return s27
    elif g36 == 13:
        return s28
    elif g36 == 14:
        return s29
    elif g36 == 15:
        return s30
    elif g36 == 16:
        return s31
    else:
        return s32


min_ajustado = calc_minimo_ajustado(g36, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32)
i36 = min_ajustado


def calc_max_ajustado(g36):
    if g36 == 0:
        return 0
    elif g36 == 4:
        return t19
    elif g36 == 5:
        return t20
    elif g36 == 6:
        return t21
    elif g36 == 7:
        return t22
    elif g36 == 8:
        return t23
    elif g36 == 9:
        return t24
    elif g36 == 10:
        return t25
    elif g36 == 11:
        return t26
    elif g36 == 12:
        return t27
    elif g36 == 13:
        return t28
    elif g36 == 14:
        return t29
    elif g36 == 15:
        return t30
    elif g36 == 16:
        return t31
    else:
        return t32


max_ajustado = calc_max_ajustado(g36)
i37 = max_ajustado


def calcular_ina(B36, Q3, B3, I36, I37):
    if B36 > Q3:
        return "pH acima do range tabelado"
    else:
        return I36 + (B36 - B3) * (I37 - I36) / (Q3 - B3)


INA = calcular_ina(b36, q3, b3, i36, i37)


print("resultado_temp_superior:  ", resultado_temp_superior)

print("resultado_temp_inferior:  ", resultado_temp_inferior)

print("resultado_guide_line:  ", resultado_guide_line)
print("-------------------------------------------------------------------")

print("                resultado_ajuste_min:  "," resultado_ajuste_max:  ")
print("Guide line 4:  ", ajuste_min_4, "  ", ajuste_max_4)
print("Guide line 5:  ", ajuste_min_5, "  ", ajuste_max_5)
print("Guide line 6:  ", ajuste_min_6, "  ", ajuste_max_6)
print("Guide line 7:  ", ajuste_min_7, "  ", ajuste_max_7)
print("Guide line 8:  ", ajuste_min_8, "  ", ajuste_max_8)
print("Guide line 8:  ", ajuste_min_9, "  ", ajuste_max_9)
print("Guide line 8:  ", ajuste_min_10, "  ", ajuste_max_10)
print("Guide line 8:  ", ajuste_min_11, "  ", ajuste_max_11)
print("Guide line 8:  ", ajuste_min_12, "  ", ajuste_max_12)
print("Guide line 8:  ", ajuste_min_13, "  ", ajuste_max_13)
print("Guide line 8:  ", ajuste_min_14, "  ", ajuste_max_14)
print("Guide line 8:  ", ajuste_min_15, "  ", ajuste_max_15)
print("Guide line 8:  ", ajuste_min_16, "  ", ajuste_max_16)
print("Guide line 8:  ", ajuste_min_17, "  ", ajuste_max_17)
print("-------------------------------------------------------------------")
print("Mínimo ajustado:  ", min_ajustado)
print("Máximo ajustado:  ", max_ajustado)
print("-------------------------------------------------------------------")
print("INA Calculado:  ", INA, "  ppm")
print("-------------------------------------------------------------------")

