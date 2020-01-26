#!/usr/bin/python3
# -*- coding: utf-8 -*-

r"""Pychemqt, Chemical Engineering Process simulator
Copyright (C) 2009-2017, Juan José Gómez Romera <jjgomera@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""


from lib.EoS.Cubic.SRK import SRK


# Paramters from [4]_, Table 1
dat = {
    2: (0.463100, 0.069800),
    3: (0.555800, 0.120800),
    4: (0.603800, 0.156300),
    6: (0.660100, 0.178900),
    5: (0.625100, 0.181800),
    8: (0.709400, 0.210300),
    7: (0.686000, 0.196000),
    9: (0.588700, 0.221700),
    10: (0.744600, 0.247600),
    52: (0.721200, 0.236300),
    53: (0.724500, 0.226900),
    54: (0.664500, 0.215800),
    55: (0.692300, 0.216200),
    11: (0.784100, 0.282800),
    79: (0.771000, 0.267500),
    80: (0.766700, 0.261900),
    436: (0.740500, 0.263500),
    432: (0.722300, 0.246500),
    433: (0.742100, 0.244700),
    434: (0.733700, 0.258500),
    435: (0.722800, 0.221400),
    437: (0.695400, 0.218200),
    12: (0.825300, 0.316400),
    81: (0.814900, 0.298700),
    590: (0.799200, 0.299500),
    591: (0.799900, 0.300200),
    598: (0.790900, 0.293400),
    592: (0.759400, 0.285600),
    593: (0.783500, 0.279800),
    594: (0.768800, 0.285800),
    595: (0.784700, 0.291100),
    596: (0.763200, 0.261100),
    597: (0.776100, 0.274800),
    601: (0.765400, 0.271300),
    602: (0.766500, 0.237300),
    541: (0.731300, 0.253500),
    82: (0.747700, 0.249800),
    599: (0.747700, 0.233000),
    600: (0.761000, 0.255800),
    603: (0.551500, 0.313900),
    13: (0.867500, 0.347200),
    370: (0.758200, 0.311800),
    369: (0.748600, 0.309100),
    # 1720: (0.784300, 0.274400), # 2,4,4-trimethylhexane
    371: (0.834300, 0.233400),
    372: (0.671500, 0.274400),
    373: (0.738100, 0.266600),
    374: (0.740800, 0.270100),
    375: (0.719300, 0.266000),
    14: (0.890500, 0.386300),
    15: (0.946700, 0.409100),
    16: (0.960400, 0.447900),
    17: (1.021200, 0.468600),
    18: (1.080400, 0.483000),
    19: (1.110400, 0.513200),
    20: (1.127400, 0.550600),
    21: (1.141400, 0.572800),
    90: (1.099200, 0.629000),
    91: (1.014100, 0.721300),
    92: (1.068200, 0.793100),
    611: (0.829000, 0.344600),
    # 850: (0.825100, 0.335300),  # 3-methyloctane
    # 851: (0.836400, 0.327400),  # 4-methyloctane
    # 1451: (0.852000, 0.308800),  # 3-ethylheptane
    # : (0.870200, 0.295500),  # 4-ethylheptane
    612: (0.759600, 0.336800),
    # : (0.816700, 0.305600),  # 2,3-dimethylheptane
    # : (0.775000, 0.342600),  # 2,4-dimethylheptane
    # : (0.773800, 0.340200),  # 2,5-dimethylheptane
    36: (0.633300, 0.190600),
    37: (0.661100, 0.216800),
    59: (0.711600, 0.233100),
    93: (0.753100, 0.201200),
    94: (0.723700, 0.220800),
    95: (0.734000, 0.214100),
    96: (0.800400, 0.186300),
    97: (0.717100, 0.221100),
    179: (0.650500, 0.300200),
    583: (0.628500, 0.277500),
    # 1716: (0.653000, 0.337600),  # n-butylcyclopentane
    398: (0.889000, 0.371400),
    401: (0.905100, 0.414400),
    407: (0.963400, 0.442800),
    410: (0.949500, 0.498000),
    38: (0.605600, 0.228200),
    39: (0.662000, 0.222400),
    60: (0.579100, 0.296000),
    87: (0.616300, 0.259500),
    88: (0.583000, 0.285200),
    577: (0.631700, 0.256300),
    89: (0.604100, 0.274800),
    84: (0.563000, 0.297300),
    85: (0.571300, 0.290200),
    86: (0.627100, 0.259000),
    184: (0.518900, 0.354800),
    190: (0.837400, 0.260300),
    22: (0.520200, 0.130000),
    23: (0.588300, 0.156700),
    24: (0.634100, 0.184900),
    25: (0.638300, 0.196600),
    26: (0.714100, 0.161400),
    27: (0.643500, 0.183300),
    29: (0.693000, 0.201100),
    30: (0.667900, 0.225400),
    31: (0.673800, 0.218600),
    32: (0.647800, 0.230800),
    33: (0.709900, 0.178200),
    34: (0.650100, 0.236800),
    35: (0.731800, 0.235900),
    552: (0.797500, 0.209600),
    553: (0.743500, 0.239200),
    554: (0.770400, 0.224300),
    65: (0.655300, 0.167200),
    66: (0.624500, 0.219200),
    67: (0.187700, 0.346800),
    151: (0.389800, 0.292800),
    299: (0.404800, 0.331300),
    # : (0.3909, 0.3174),  # 2-pentyne
    # 1349: (0.9930, 0.0104),  # 3-hexyne
    40: (0.604300, 0.228500),
    41: (0.711700, 0.224200),
    45: (0.745800, 0.251200),
    42: (0.773700, 0.241500),
    43: (0.801100, 0.242100),
    44: (0.794100, 0.240000),
    70: (0.792100, 0.271200),
    71: (0.740200, 0.284000),
    72: (0.744200, 0.308700),
    73: (0.669600, 0.349100),
    74: (0.764200, 0.300400),
    75: (0.856900, 0.254200),
    76: (0.868200, 0.260200),
    77: (0.898700, 0.266300),
    78: (0.846000, 0.295200),
    377: (0.886600, 0.246900),
    378: (0.835400, 0.270900),
    379: (0.746500, 0.301200),
    380: (0.881700, 0.261600),
    381: (0.872500, 0.261300),
    382: (0.835300, 0.277700),
    194: (0.827400, 0.276200),
    406: (0.981500, 0.302100),
    185: (0.756600, 0.242700),
    191: (1.016300, 0.220000),
    200: (0.968500, 0.228400),
    117: (1.301300, 0.200500),
    134: (1.154500, 0.404700),
    146: (0.691700, 0.695800),
    145: (0.643400, 0.785400),
    159: (0.345300, 0.898900),
    161: (0.237400, 1.003500),
    160: (0.415100, 0.850600),
    450: (0.433700, 0.848300),
    174: (0.837200, 0.356600),
    177: (0.827600, 0.357000),
    346: (0.726000, 0.454000),
    347: (0.939100, 0.371700),
    140: (0.795100, 0.220500),
    153: (0.779300, 0.250700),
    304: (0.784500, 0.279600),
    165: (0.756400, 0.295000),
    329: (0.829900, 0.288900),
    133: (0.672000, 0.172700),
    486: (0.955000, 0.033900),
    162: (0.747300, 0.227900),
    318: (0.830900, 0.230700),
    337: (0.726600, 0.297300),
    129: (0.673900, 0.171600),
    131: (0.728000, 0.211900),
    141: (0.617200, 0.308300),
    157: (0.627800, 0.338000),
    142: (0.741700, 0.277700),
    155: (0.762300, 0.314200),
    166: (0.767200, 0.345700),
    156: (0.728300, 0.317400),
    309: (0.772400, 0.343900),
    118: (0.713100, 0.260200),
    249: (0.582700, 0.350900),
    147: (0.643700, 0.190900),
    138: (0.702200, 0.269300),
    294: (0.542500, 0.387700),
    270: (0.534200, 0.369800),
    # 225: (0.644100, 0.172300),
    # 643: (0.769900, 0.185300),
    # 218: (0.671500, 0.149600),
    # 247: (0.784700, 0.197400),
    # 245: (0.590600, 0.276400),
    # 243: (0.724900, 0.204100),
    # 693: (0.662300, 0.391800),
    # 321: (1.182200, 0.249900),
    # 322: (0.751300, 0.188300),
    # 642: (0.656000, 0.202100),
    # 220: (0.665000, 0.201300),
    # 216: (0.560500, 0.215600),
    # 217: (0.630200, 0.183800),
    # 234: (0.705800, 0.253700),
    # 232: (0.638000, 0.261000),
    # 231: (0.611400, 0.277200),
    # 229: (0.742700, 0.199500),
    # 215: (0.701200, 0.205600),
    115: (0.620500, 0.150300),
    222: (0.718300, 0.150100),
    112: (0.681600, 0.188300),
    100: (0.609200, 0.202600),
    132: (0.651800, 0.174300),
    126: (0.740400, 0.177900),
    127: (0.876700, 0.144400),
    479: (0.609400, 0.219600),
    122: (0.485900, 0.201200),
    658: (0.604900, 0.197300),
    659: (0.715600, 0.157400),
    119: (0.625200, 0.249800),
    172: (0.671700, 0.231800),
    224: (0.310400, 0.250100),
    171: (0.690600, 0.219600),
    116: (0.372900, 0.235700),
    136: (0.618000, 0.194700),
    269: (0.563800, 0.259900),
    290: (0.760300, 0.227200),
    # : (0.5777, 0.2713),   # methyl propyl sulfide
    # : (0.6667, 0.2416),   # methyl isopropyl sulfide
    227: (0.591200, 0.164300),
    137: (0.608600, 0.198400),
    # 1296: (0.6738, 0.2497),   # 2-methyl-2-propylthiol
    743: (0.745100, 0.264900),
    113: (1.349800, -0.040600),
    226: (0.993800, 0.129600),
    46: (0.446800, 0.109300),
    47: (0.487100, 0.071700),
    105: (0.459700, 0.154300),
    # 994: (0.4304, 0.0834),   # xenon
    1: (0.256300, -0.074200),
    62: (0.949900, 0.163300),
    49: (0.580900, 0.272700),
    110: (0.058700, 0.497100),
    51: (0.635800, 0.261400),
    50: (0.459400, 0.179000),
    102: (0.621100, 0.091000),
    104: (0.628800, 0.112400),
    63: (0.783800, 0.160400),
    630: (0.707600, 0.429200),
    # 951: (0.6878, 0.0952),   # nitrogen trifluoride
    # : (0.7958, 0.1473),  # boron tribromide
    219: (0.536800, 0.138700),

    # Aditional parameters for CFCs from [5]_, Table 2
    239: (0.7381, 0.0553),
    242: (0.5176, 0.2169),
    215: (0.6176, 0.1737),
    218: (0.6635, 0.1515),
    216: (0.6129, 0.1848),
    217: (0.6336, 0.1819),
    225: (0.7056, 0.1372),
    642: (0.6310, 0.2083),
    247: (0.7054, 0.1775),
    654: (0.6449, 0.2152),
    220: (0.666, 0.2001),
    # r113a: (0.674, 0.2018),
    # r151: (0.6628, 0.2163),
    235: (0.6867, 0.207),
    652: (0.6747, 0.2165),
    241: (0.71165, 0.1866),
    322: (0.7393, 0.1941),
    # r1112: (0.6902, 0.2164),
    243: (0.6964, 0.2136),
    230: (0.7008, 0.2167),
    229: (0.7076, 0.2137),
    232: (0.7076, 0.2167),
    231: (0.7074, 0.2168),
    245: (0.7484, 0.1952),
    236: (0.7372, 0.1977),
    643: (0.7962, 0.1723),
    # r132b: (0.7868, 0.1869),
    # 1242: (0.7584, 0.2043),
    645: (0.8503, 0.1498),
    # 1870: (0.7692, 0.2072),
    # r124a: (0.7998, 0.1938),
    234: (0.859, 0.2122),
    # chloropentafluoroacetone: (0.7018, 0.3309),
    692: (0.7198, 0.3375),
    693: (0.8271, 0.2845),
    319: (0.8516, 0.3009),
    # perfluropentane: (0.6569, 0.4611),
    320: (1.1143, 0.1635),
    340: (1.2063, 0.1657),
    321: (0.8998, 0.3877),
    326: (0.9354, 0.4432),
    }

# Procedure to calculate parameters from vapor pressure experimental data
# Soave, G.
# Rigorous and Simplified Procedures for Determining the Pure-Component
# Parameters in the Redlich-Kwong-Soave Equation of State.
# Chem. Eng. Sci. 35(8) (1980) 1725-1729
# 10.1016/0009-2509(80)85007-x


class MSRK(SRK):
    r"""Modified SRK two parameters cubic equation of state as explain in [1]_

    .. math::
        \begin{array}[t]{l}
        P = \frac{RT}{V-b}-\frac{a}{V\left(V+b\right)}\\
        a = 0.42747\frac{R^2T_c^2}{P_c}\alpha\\
        b = 0.08664\frac{RT_c}{P_c}\\
        \alpha = 1 + m\left(1-Tr\right) + n\left(\frac{1}{T_R}-1\right)\\
        \end{array}

    m and n are compound specific parameters, compiled from [4]_ and [5]_

    Examples
    --------
    Example 4.3 from [2]_, Propane saturated at 300K

    >>> from lib.mezcla import Mezcla
    >>> mix = Mezcla(5, ids=[4], caudalMolar=1, fraccionMolar=[1])
    >>> eq = MSRK(300, 9.9742e5, mix)
    >>> '%0.0f %0.1f' % (eq.Vg.ccmol, eq.Vl.ccmol)
    '2063 98.2'
    >>> eq = MSRK(300, 42.477e5, mix)
    >>> '%0.1f' % (eq.Vl.ccmol)
    '94.9'
    """
    __title__ = "M-SRK (1979)"
    __status__ = "MSRK"
    __doi__ = (
      {
         "autor": "Soave, G.",
         "title": "Application of a Cubic Equation of State to Vapor-Liquid "
                  "Equilibria of Systems Containing Polar Compounds",
         "ref": "Inst. Chem. Eng. Symp. Ser. 56 (1979) 1.2/1-1.2/16",
         "doi": ""},
      {
        "autor": "Soave, G.",
        "title": "Improvement of the van der Waals Equation of State",
        "ref": "Chem. Eng. Sci. 39(2) (1984) 357-369",
        "doi": "10.1016/0009-2509(84)80034-2"},
      {
         "autor": "Poling, B.E, Prausnitz, J.M, O'Connell, J.P",
         "title": "The Properties of Gases and Liquids 5th Edition",
         "ref": "McGraw-Hill, New York, 2001",
         "doi": ""},
      {
         "autor": "Sandarusi, J.A., Kidnay, A.J., Yesavage, V.F.",
         "title": "Compilation of Parameters for a Polar Fluid Soave-Redlich-"
                  "Kwong Equation of State",
         "ref": "Ind. Eng. Chem. Process Des. Dev. 25(4) (1986) 957-963",
         "doi": "10.1021/i200035a020"},
      {
         "autor": "Kadhem, Q.M.A, Al-Sahhaf, T.A., Hamam, S.E.M.",
         "title": "Parameters of the Modified Soave-Redlich-Kwong Equation of "
                  "State for Some Chlorofluorocarbons, Hydrofluorocarbons and"
                  "Fluorocarbons",
         "ref": "J. Fluorine Chem. 43(1) (1989) 87-104",
         "doi": "10.1016/s0022-1139(00)81638-3"},
      {
         "autor": "",
         "title": "",
         "ref": "",
         "doi": ""},
      )

    def _alfa(self, cmp, T):
        """Special alpha function for this modified version, if the compound
        specified parameters are not available in database use the standard
        SRK alpha expresion"""
        if cmp.id in dat:
            m, n = dat[cmp.id]
            alfa = 1 + m*(1-T/cmp.Tc) + n*(cmp.Tc/T-1)                  # Eq 7
        else:
            alfa = SRK._alfa(self, cmp, T)
        return alfa


if __name__ == "__main__":
    from lib.mezcla import Mezcla
    mix = Mezcla(5, ids=[4], caudalMolar=1, fraccionMolar=[1])
    eq = MSRK(300, 9.9742e5, mix)
    print('%0.0f %0.1f' % (eq.Vg.ccmol, eq.Vl.ccmol))
    eq = MSRK(300, 42.477e5, mix)
    print('%0.1f' % (eq.Vl.ccmol))
