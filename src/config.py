# Random seed and paths
RANDOM_SEED = 42

# Columns
COL_LANGUAGE = "Language"
COL_MACROAREA = "Macroarea"
COL_NUM = "GB024"
COL_DEM = "GB025"

# Primary sample: unique unmarked orders only
STRICT_NUM = {"Num-N", "N-Num"}
STRICT_DEM = {"Dem-N", "N-Dem"}

HARMONIOUS = {
    ("Num-N", "Dem-N"),
    ("N-Num", "N-Dem"),
}
