import copy

from CostFunctions.CostFunctions import CostFunctions

# from CostFunctions.simpleQuadratic import simpleQuadratic
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
from CostFunctions.Mishra9 import Mishra9
from CostFunctions.Mishra10a import Mishra10a
from CostFunctions.Mishra10b import Mishra10b
from CostFunctions.Mishra11 import Mishra11N2, Mishra11N6, Mishra11N10, Mishra11N20
from CostFunctions.Parsopoulos import Parsopoulos
from CostFunctions.PenHolder import PenHolder
from CostFunctions.Pathological import PathologicalN2, PathologicalN6, PathologicalN10, PathologicalN20
from CostFunctions.Pinter import PinterN2, PinterN6, PinterN10, PinterN20
from CostFunctions.Periodic import Periodic
from CostFunctions.PowellSingular import PowellSingular
from CostFunctions.PowellSum import PowellSumN2, PowellSumN6, PowellSumN10, PowellSumN20
from CostFunctions.Price1 import Price1
from CostFunctions.Price2 import Price2
from CostFunctions.Price3 import Price3
from CostFunctions.Price4 import Price4
from CostFunctions.Ripple1 import Ripple1N2, Ripple1N6, Ripple1N10, Ripple1N20
from CostFunctions.Ripple25 import Ripple25N2, Ripple25N6, Ripple25N10, Ripple25N20
from CostFunctions.RotatedEllipse import RotatedEllipse
from CostFunctions.Qing import QingN2, QingN6, QingN10, QingN20
from CostFunctions.Quadratic import Quadratic
from CostFunctions.Quintic import QuinticN2, QuinticN6, QuinticN10, QuinticN20
from CostFunctions.Quartic import QuarticN2, QuarticN6, QuarticN10, QuarticN20
from CostFunctions.RotatedEllipse2 import RotatedEllipse2
from CostFunctions.Rump import Rump
from CostFunctions.Salomon import SalomonN2, SalomonN6, SalomonN10, SalomonN20
from CostFunctions.Sargan import SarganN2, SarganN6, SarganN10, SarganN20
from CostFunctions.Scahffer1 import Scahffer1
from CostFunctions.Scahffer2 import Scahffer2
from CostFunctions.Scahffer3 import Scahffer3
from CostFunctions.Scahffer4 import Scahffer4
from CostFunctions.SchmidtVetters import SchmidtVetters
from CostFunctions.SchumerSteiglitz import SchumerSteiglitzN2, SchumerSteiglitzN6, SchumerSteiglitzN10, SchumerSteiglitzN20
from CostFunctions.Schwefel import SchwefelN2, SchwefelN6, SchwefelN10, SchwefelN20
from CostFunctions.Schwefel1d2 import Schwefel1d2N2, Schwefel1d2N6, Schwefel1d2N10, Schwefel1d2N20
from CostFunctions.Schwefel2d4 import Schwefel2d4N2, Schwefel2d4N6, Schwefel2d4N10, Schwefel2d4N20
from CostFunctions.Schwefel2d6 import Schwefel2d6
from CostFunctions.Schwefel2d20 import Schwefel2d20N2, Schwefel2d20N6, Schwefel2d20N10, Schwefel2d20N20
from CostFunctions.Schwefel2d21 import Schwefel2d21N2, Schwefel2d21N6, Schwefel2d21N10, Schwefel2d21N20
from CostFunctions.Schwefel2d22 import Schwefel2d22N2, Schwefel2d22N6, Schwefel2d22N10, Schwefel2d22N20
from CostFunctions.Schwefel2d23 import Schwefel2d23N2, Schwefel2d23N6, Schwefel2d23N10, Schwefel2d23N20
from CostFunctions.Schwefel2d26 import Schwefel2d26N2, Schwefel2d26N6, Schwefel2d26N10, Schwefel2d26N20
from CostFunctions.Schwefel2d36 import Schwefel2d36
from CostFunctions.Shekel5 import Shekel5
from CostFunctions.Shekel7 import Shekel7
from CostFunctions.Shekel10 import Shekel10
from CostFunctions.Shubert import Shubert
from CostFunctions.SchafferF6 import SchafferF6
from CostFunctions.Sphere import SphereN2, SphereN6, SphereN10, SphereN20
#Removed because they have an infinite number of solutions
# from CostFunctions.Step import StepN2, StepN6, StepN10, StepN20
# from CostFunctions.Step2 import Step2N2, Step2N6, Step2N10, Step2N20
# from CostFunctions.Step3 import Step3N2, Step3N6, Step3N10, Step3N20
from CostFunctions.StrechedVSineWave2N import StrechedVSineWave2N
from CostFunctions.SumSquares import SumSquaresN2, SumSquaresN6, SumSquaresN10, SumSquaresN20
from CostFunctions.StyblinkskiTang import StyblinkskiTang
from CostFunctions.Table1 import Table1
from CostFunctions.Table2 import Table2
from CostFunctions.Table3 import Table3
from CostFunctions.TesttubeHolder import TesttubeHolder
from CostFunctions.Trecanni import Trecanni
from CostFunctions.Trefethen import Trefethen
from CostFunctions.Trigonometric1 import Trigonometric1N2, Trigonometric1N6, Trigonometric1N10, Trigonometric1N20
from CostFunctions.Trigonometric2 import Trigonometric2N2, Trigonometric2N6, Trigonometric2N10, Trigonometric2N20
from CostFunctions.Tripod import Tripod
from CostFunctions.Ursem1 import Ursem1
from CostFunctions.Ursem3 import Ursem3
from CostFunctions.Ursem4 import Ursem4
from CostFunctions.UrsemWaves import UrsemWaves
from CostFunctions.VenterSobiezcczanskiSobieski import VenterSobiezcczanskiSobieski
from CostFunctions.Watson import Watson


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
    'Mishra8',
    'Mishra9',
    'Mishra10a',
    'Mishra10b',
    'Mishra11N2', 'Mishra11N6', 'Mishra11N10', 'Mishra11N20',
    'Parsopoulos',
    'PenHolder',
    'PathologicalN2', 'PathologicalN6', 'PathologicalN10', 'PathologicalN20',
    'PinterN2', 'PinterN6', 'PinterN10', 'PinterN20',
    'Periodic',
    'PowellSingular',
    'PowellSumN2', 'PowellSumN6', 'PowellSumN10', 'PowellSumN20',
    'Price1',
    'Price2',
    'Price3',
    'Price4',
    # 'Ripple1N2', 'Ripple1N6', 'Ripple1N10', 'Ripple1N20', # Problems in finding the minimum (there are others)
    # 'Ripple25N2', 'Ripple25N6', 'Ripple25N10', 'Ripple25N20', # Problems in finding the minimum (there are others)
    'RotatedEllipse',
    'QingN2', 'QingN6', 'QingN10', 'QingN20',
    'Quadratic',
    'QuinticN2', 'QuinticN6', 'QuinticN10', 'QuinticN20',
    'QuarticN2', 'QuarticN6', 'QuarticN10', 'QuarticN20',
    'RotatedEllipse2',
    # 'Rump' , # Problems in finding the minimum (there are others)
    'SalomonN2', 'SalomonN6', 'SalomonN10', 'SalomonN20',
    'SarganN2', 'SarganN6', 'SarganN10', 'SarganN20',
    'Scahffer1',
    'Scahffer2',
    'Scahffer3',
    'Scahffer4',
    'SchumerSteiglitzN2', 'SchumerSteiglitzN6', 'SchumerSteiglitzN10', 'SchumerSteiglitzN20',
    'SchwefelN2', 'SchwefelN6', 'SchwefelN10', 'SchwefelN20',
    'Schwefel1d2N2', 'Schwefel1d2N6', 'Schwefel1d2N10', 'Schwefel1d2N20',
    'Schwefel2d4N2', 'Schwefel2d4N6', 'Schwefel2d4N10', 'Schwefel2d4N20',
    'Schwefel2d6',
    'Schwefel2d20N2', 'Schwefel2d20N6', 'Schwefel2d20N10', 'Schwefel2d20N20',
    'Schwefel2d21N2', 'Schwefel2d21N6', 'Schwefel2d21N10', 'Schwefel2d21N20',
    'Schwefel2d22N2', 'Schwefel2d22N6', 'Schwefel2d22N10', 'Schwefel2d22N20',
    'Schwefel2d23N2', 'Schwefel2d23N6', 'Schwefel2d23N10', 'Schwefel2d23N20',
    'Schwefel2d26N2', 'Schwefel2d26N6', 'Schwefel2d26N10', 'Schwefel2d26N20',
    'Schwefel2d36',
    'Shekel5',
    'Shekel7',
    'Shekel10',
    'Shubert',
    'SchafferF6',
    'SphereN2', 'SphereN6', 'SphereN10', 'SphereN20',
    # 'StepN2', 'StepN6', 'StepN10', 'StepN20',
    # 'Step2N2', 'Step2N6', 'Step2N10', 'Step2N20',
    # 'Step3N2', 'Step3N6', 'Step3N10', 'Step3N20',
    'StrechedVSineWave2N',
    'SumSquaresN2', 'SumSquaresN6', 'SumSquaresN10', 'SumSquaresN20',
    'StyblinkskiTang',
    'Table1',
    'Table2',
    'Table3',
    'TesttubeHolder',
    'Trefethen',
    'Trigonometric1N2', 'Trigonometric1N6', 'Trigonometric1N10', 'Trigonometric1N20',
    'Trigonometric2N2', 'Trigonometric2N6', 'Trigonometric2N10', 'Trigonometric2N20',
    'Tripod',
    'Ursem1',
    'Ursem3',
    'Ursem4',
    'UrsemWaves',
    'VenterSobiezcczanskiSobieski',
    'Watson'
    ]

all_variables = copy.copy(all_benchmarks)
all_variables.append('all_benchmarks')
all_variables.append('CostFunctions')
__all__ = all_variables
