from blosum62 import BLOSUM62
from needleman_wunsch import needleman_wunsch

sequencia_v = "DRQTAQAAGTTTIT"
sequencia_w = "DRNTAQLLGTDTT"

needleman_wunsch(sequencia_v, sequencia_w, BLOSUM62)
