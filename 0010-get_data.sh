
# Drug - mechanism of action
rsync -rpltvz --delete rsync.ebi.ac.uk::pub/databases/opentargets/platform/21.04/output/etl/json/mechanismOfAction .

# Drug - indications
rsync -rpltvz --delete rsync.ebi.ac.uk::pub/databases/opentargets/platform/21.04/output/etl/json/indication .

# Drug - withdrawn and black box warnings
rsync -rpltvz --delete rsync.ebi.ac.uk::pub/databases/opentargets/platform/21.04/output/etl/json/drugWarnings .

# Core annotation for drug molecules
rsync -rpltvz --delete rsync.ebi.ac.uk::pub/databases/opentargets/platform/21.04/output/etl/json/molecule .
