
# mega-checker
check if mega link is valid or dead (either one link or a txt file)


## Installation
clone the repo
```
git clone https://github.com/Titoot/mega-checker.git
cd mega-checker
```
to install required libraries
```
pip install -r requirements.txt
```

then run it
```
python mega.py -h
```
# Guide

one url
```
python mega.py -u <url>
```
file
```
python mega.py -i <file>
```

you can use test.txt as an example

```
https://mega.nz/#!oMhDAAqC!XQqMb9u7oAKvYMYYRHYI_s870Y2wXR4bzlL4aQI1eps | valid
https://mega.nz/#!ddg0HSJB!t9L3mrMiWGJJRk0tYxR-9Vpfd3fXWkywy3cjaoY_eRY | not valid
https://mega.nz/#!NmwjyDTT!yzPoKFITz2rcM7EogkgThMjuwQi7Q1aSJCqJneG2Xe0 | not valid
https://mega.nz/#!oYBnwAoC!k1mvu2VM-kcnQrNF4jKDgQdAWBL_smlwf_q11M-tsHk | not valid
https://mega.nz/#!5EBGXYoI!J1fZBU_qZ2mhg-jUV2E4caCHDoLy5YesDh1QF6hw0Z8 | not valid
https://mega.nz/#!IdwjFJqR!ShCPhpSdM2z3PVvUHAEC3Lt6XAKeHAdzY7ZHgSGMa2k | not valid
https://mega.nz/#!giRyVI7a!FJ_R_OOM2_bBewCASmnZCSYBZPyeViiEFvp0xUP7TL4 | not valid
https://mega.nz/#!hMhR3aiI!k5r_RHdDgqxDz5DZOFKPf1QK12Lz89XjMULKChBchi4 | valid
https://mega.nz/#!8JBT0CiK!_xdw2QEbdS4s4FNAUpBHYYPnqCsLvbVwmqyWn1Un5qo | valid
https://mega.nz/#!VMgjGAjJ!FpjhQ32t3a6UhVrREPtm4oXUZ8a6lXzhAXkbsenNkt0 | valid
https://mega.nz/#!FUBwWKbD!i1qE6gQvvk0_mIr8O1rhoN9LXUu6AKmn7Rvyz8slt- | valid
```

## to-do

- [ ] add drive links support



<!--- CRINGE
#### donate if you liked what i do :)
#### bitcoin:
#### bc1q773tfvtmuefey2rc2smh98m6xtcuza29xfgfyw
#### ETH:
#### 0xf09B18434F441E49fc90BE141b2Ba3877c1C1b2d
#### you don't have to --->
