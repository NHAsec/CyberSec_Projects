import wmi

c = wmi.WMI()

print("Antivirus check is running")

AV_Check = [
 "MsMpEng.exe", "AdAwareService.exe", "afwServ.exe", "avguard.exe", "AVGSvc.exe",
 "bdagent.exe", "BullGuardCore.exe", "ekrn.exe", "fshoster32.exe", "GDScan.exe", 
 "avp.exe", "K7CrvSvc.exe", "McAPExe.exe", "NortonSecurity.exe", "PavFnSvr.exe", 
 "SavService.exe", "EnterpriseService.exe", "WRSA.exe", "ZAPrivacyService.exe"
] 

n = 0
trig = False

for process in c.query("SELECT * from win32_process"):
	if process.Name in AV_Check:
		print(f"--AV Found: {n}, {process.Name} (PID: {process.ProcessId})")
		trig = True
	n += 1

if not trig:
	print("--AV software is not found!")
