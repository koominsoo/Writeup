import angr

def main():
	p=angr.Project("./a.out")
	simgr=p.factory.simulation_manager(p.factory.full_init_state())
	simgr.explore(find=0x40111d,avoid=0x401100)
	return simgr.found[0].posix.dumps(0).strip(b'\0\n')
if __name__=='__main__':
	main()

