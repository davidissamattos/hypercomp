import copy

from CostFunctions.CostFunctions import CostFunctions

from CostFunctions.simpleQuadratic import simpleQuadratic
from CostFunctions.Ackley1 import Ackley1N2,Ackley1N6,Ackley1N10,Ackley1N20
from CostFunctions.Ackley2 import Ackley2
from CostFunctions.Ackley3 import Ackley3
from CostFunctions.Adjiman import Adjiman
from CostFunctions.Alpine1 import Alpine1N2, Alpine1N6, Alpine1N10, Alpine1N20
from CostFunctions.Alpine2 import Alpine2
from CostFunctions.BartelsConn import BartelsConn
from CostFunctions.Beale import Beale
from CostFunctions.BiggsEXP2 import BiggsEXP2
from CostFunctions.BiggsEXP3 import BiggsEXP3
from CostFunctions.BiggsEXP4 import BiggsEXP4
from CostFunctions.BiggsEXP5 import BiggsEXP5
from CostFunctions.BiggsEXP6 import BiggsEXP6
from CostFunctions.Bird import Bird
# from CostFunctions.__Brad import Brad
from CostFunctions.Easom import Easom
from CostFunctions.BraninRCOS import BraninRCOS
from CostFunctions.BraninRCOS2 import BraninRCOS2
from CostFunctions.Easom import Easom
from CostFunctions.Miele import Miele
from CostFunctions.Paviani import Paviani
from CostFunctions.Rosenbrock import RosenbrockN2,RosenbrockN6, RosenbrockN10, RosenbrockN20
from CostFunctions.RosenbrockModified import RosenbrockModified
from CostFunctions.SixHumpCamelBack import SixHumpCamelBack
from CostFunctions.ThreeHumpCamelBack import ThreeHumpCamelBack
from CostFunctions.ChenBird import ChenBird
from CostFunctions.ChenV import ChenV
from CostFunctions.Bohachevsky1 import Bohachevsky1
from CostFunctions.Bohachevsky2 import Bohachevsky2
from CostFunctions.Bohachevsky3 import Bohachevsky3
from CostFunctions.Booth import Booth
from CostFunctions.BoxBettsQuadraticSum import BoxBettsQuadraticSum
from CostFunctions.Brent import Brent
from CostFunctions.Brown import BrownN2, BrownN6, BrownN10, BrownN20
from CostFunctions.Bunkin2 import Bunkin2
from CostFunctions.Bunkin4 import Bunkin4
from CostFunctions.Bunkin6 import Bunkin6
from CostFunctions.Chichinadze import Chichinadze
from CostFunctions.ChungReynolds import ChungReynoldsN2,ChungReynoldsN6,ChungReynoldsN10,ChungReynoldsN20
from CostFunctions.Colville import Colville
from CostFunctions.Corana import Corana
from CostFunctions.CosineMixture import CosineMixtureN2, CosineMixtureN6, CosineMixtureN10, CosineMixtureN20
from CostFunctions.CrossInTray import CrossInTray
from CostFunctions.Csendes import CsendesN2,CsendesN6,CsendesN10,CsendesN20
from CostFunctions.Cube import Cube
from CostFunctions.Damavandi import Damavandi
from CostFunctions.DeckkersAarts import DeckkersAarts
from CostFunctions.DixonPrice import DixonPriceN2,DixonPriceN6,DixonPriceN10,DixonPriceN20
from CostFunctions.Dolan import Dolan
from CostFunctions.DeVilliersGlasser01 import DeVilliersGlasser01
from CostFunctions.DeVilliersGlasser02 import DeVilliersGlasser02
from CostFunctions.ElAttarVidyasagarDutta import ElAttarVidyasagarDutta
from CostFunctions.EggCrate import EggCrate
from CostFunctions.EggHolder import EggHolder
from CostFunctions.Exponential import ExponentialN2,ExponentialN6,ExponentialN10,ExponentialN20
from CostFunctions.Exp2 import Exp2
from CostFunctions.FreudensteinRoth import FreudensteinRoth
from CostFunctions.Giunta import Giunta
from CostFunctions.GoldsteinPrice import GoldsteinPrice
from CostFunctions.Griewank import GriewankN2,GriewankN6,GriewankN10,GriewankN20
from CostFunctions.GulfResearch import GulfResearch
from CostFunctions.Hansen import Hansen
from CostFunctions.Hartman3 import Hartman3
from CostFunctions.Hartman6 import Hartman6
from CostFunctions.HelicalValley import HelicalValley
from CostFunctions.Cola import Cola
from CostFunctions.Himmelblau import Himmelblau
from CostFunctions.Hosaki import Hosaki
from CostFunctions.JennrichSampson import JennrichSampson
from CostFunctions.Langerman import Langerman
from CostFunctions.Keane import Keane
from CostFunctions.Leon import Leon
from CostFunctions.Matyas import Matyas
from CostFunctions.McCormick import McCormick
from CostFunctions.Mishra1 import Mishra1N2, Mishra1N6, Mishra1N10, Mishra1N20
from CostFunctions.Mishra2 import Mishra2N2, Mishra2N6, Mishra2N10, Mishra2N20
from CostFunctions.Mishra3 import Mishra3
from CostFunctions.Mishra4 import Mishra4
from CostFunctions.Mishra5 import Mishra5
from CostFunctions.Mishra6 import Mishra6
from CostFunctions.Mishra7 import Mishra7N2, Mishra7N6, Mishra7N10, Mishra7N20
from CostFunctions.Mishra8 import Mishra8

all_benchmarks = [
    # 'simpleQuadratic',
    'Ackley1N2','Ackley1N6','Ackley1N10', 'Ackley1N20',
    'Ackley2',
    'Ackley3',
    'Adjiman',
    'Alpine1N2', 'Alpine1N6', 'Alpine1N10', 'Alpine1N20',
    'Alpine2',
    'BartelsConn',
    'Beale',
    'BiggsEXP2',
    'BiggsEXP3',
    'BiggsEXP4',
    'BiggsEXP5',
    'BiggsEXP6',
    'Bird',
    # 'Brad',
    'BraninRCOS',
    'BraninRCOS2',
    'Easom',
    'Miele',
    'Paviani',
    'RosenbrockN2','RosenbrockN6', 'RosenbrockN10', 'RosenbrockN20',
    'RosenbrockModified',
    'ThreeHumpCamelBack',
    'SixHumpCamelBack',
    'ChenBird',
    'ChenV',
    'Bohachevsky1',
    'Bohachevsky2',
    'Bohachevsky3',
    'Booth',
    'BoxBettsQuadraticSum',
    'Brent',
    'BrownN2', 'BrownN6', 'BrownN10', 'BrownN20',
    'Bunkin2',
    'Bunkin4',
    'Bunkin6',
    'Chichinadze',
    'ChungReynoldsN2','ChungReynoldsN6','ChungReynoldsN10','ChungReynoldsN20',
    'Colville',
    'Corana',
    'CosineMixtureN2', 'CosineMixtureN6', 'CosineMixtureN10', 'CosineMixtureN20',
    'CrossInTray',
    'CsendesN2','CsendesN6','CsendesN10','CsendesN20',
    'Cube',
    'Damavandi',
    'DeckkersAarts',
    'DixonPriceN2', 'DixonPriceN6', 'DixonPriceN10', 'DixonPriceN20',
    'Dolan',
    'DeVilliersGlasser01',
    'DeVilliersGlasser02',
    'ElAttarVidyasagarDutta',
    'EggCrate',
    'EggHolder',
    'ExponentialN2','ExponentialN6','ExponentialN10','ExponentialN20',
    'Exp2',
    'FreudensteinRoth',
    'Giunta',
    'GoldsteinPrice',
    'GriewankN2','GriewankN6','GriewankN10','GriewankN20',
    'GulfResearch',
    'Hansen',
    'Hartman3',
    'Hartman6',
    'HelicalValley',
    'Cola',
    'Himmelblau',
    'Hosaki',
    'JennrichSampson',
    'Langerman',
    'Keane',
    'Leon',
    'Matyas',
    'McCormick',
    'Mishra1N2', 'Mishra1N6', 'Mishra1N10', 'Mishra1N20',
    'Mishra2N2', 'Mishra2N6', 'Mishra2N10', 'Mishra2N20',
    'Mishra3',
    'Mishra4',
    'Mishra5',
    'Mishra6',
    'Mishra7N2', 'Mishra7N6', 'Mishra7N10', 'Mishra7N20',
    'Mishra8'
    ]

all_variables = copy.copy(all_benchmarks)
all_variables.append('all_benchmarks')
all_variables.append('CostFunctions')
__all__ = all_variables
