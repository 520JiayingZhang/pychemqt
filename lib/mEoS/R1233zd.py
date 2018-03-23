#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''Pychemqt, Chemical Engineering Process simulator
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
along with this program.  If not, see <http://www.gnu.org/licenses/>.'''


from lib.meos import MEoS
from lib import unidades


class R1233zd(MEoS):
    """Multiparameter equation of state for R1233zd"""
    name = "1-chloro-3,3,3-trifluoroprop-1-ene"
    CASNumber = "102687-65-0"
    formula = "CHCl=CH-CF3"
    synonym = "R1233zd"
    rhoc = unidades.Density(480.219392)
    Tc = unidades.Temperature(439.6)
    Pc = unidades.Pressure(3623.7, "kPa")
    M = 130.4944  # g/mol
    Tt = unidades.Temperature(195.15)
    Tb = unidades.Temperature(291.47)
    f_acent = 0.305
    momentoDipolar = unidades.DipoleMoment(1.44, "Debye")

    CP1 = {"ao": 4.0,
           "an": [], "pow": [],
           "ao_exp": [11.765, 8.6848],
           "exp": [630, 2230],
           "ao_hyp": [], "hyp": []}

    mondejar = {
        "__type__": "Helmholtz",
        "__name__": "Helmholtz equation of state for R1233zd(E) of Mondejar "
                    "(2013).",
        "__doi__": {"autor": "Mondejar, M.E., McLinden, M.O., Lemmon, E.W.",
                    "title": "Thermodynamic Properties of trans-1-Chloro-3,3,3"
                             "-trifluoropropene (R1233zd(E)): Vapor Pressure, "
                             "(p-ρ-T) Behavior, and Spped of Sound "
                             "Measurements, and Equation of State",
                    "ref": "J. Chem. Eng. Data 60(8) (2015) 2477-2489",
                    "doi": "10.1021/acs.jced.5b00348"},

        "R": 8.3144621,
        "cp": CP1,
        "ref": "IIR",

        "Tmin": Tt, "Tmax": 550.0, "Pmax": 100000.0, "rhomax": 11.41,
        "Pmin": 0.25, "rhomin": 11.41,

        "nr1": [0.0478487, 1.60644, -2.27161, -0.530687, 0.169641],
        "d1": [4, 1, 1, 2, 3],
        "t1": [1., 0.26, 1.02, 0.7, 0.4],

        "nr2": [-1.85458, -0.321916, 0.636411, -0.121482, -0.0262755],
        "d2": [1, 3, 2, 2, 7],
        "t2": [1.46, 2.3, 0.66, 2.7, 1.19],
        "c2": [2, 2, 1, 2, 1],
        "gamma2": [1]*5,

        "nr3": [2.37362, -0.901771, -0.455962, -0.602941, -0.0594311],
        "d3": [1, 1, 3, 2, 2],
        "t3": [1.62, 1.13, 1.7, 1.35, 1.5],
        "alfa3": [0.748, 1.473, 1.39, 0.86, 1.8],
        "beta3": [1.29, 1.61, 0.8, 1.34, 0.49],
        "gamma3": [0.89, 1.13, 0.7, 0.91, 1.2],
        "epsilon3": [0.508, 0.366, 0.38, 0.773, 1.17],
        "nr4": []}

    eq = mondejar,

    _vapor_Pressure = {
        "eq": 5,
        "ao": [-7.6021, 2.3265, -1.9771, -4.8451, -4.8762],
        "exp": [1.0, 1.5, 2.0, 4.3, 14.0]}
    _liquid_Density = {
        "eq": 1,
        "ao": [2.13083, 0.583568, 0.247871, 0.472173],
        "exp": [0.355, 0.9, 3.5, 8.0]}
    _vapor_Density = {
        "eq": 3,
        "ao": [-3.0152, -6.5621, -19.427, -62.650, -181.64],
        "exp": [0.397, 1.2, 3.1, 6.6, 15.0]}
