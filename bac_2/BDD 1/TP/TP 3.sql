select distinct e.job, d.loc from emp e, dept d  where e.deptno = 30 and e.deptno = d.deptno;

select e.ename, e.deptno, d.loc from  emp e, dept d where e.comm is not null and e.deptno = d.deptno

select * from emp where ename like '%A%';

select e1.* from emp e1, emp e2 where e2.ename like 'BLAkE' and e1.hiredate >= e2.hiredate;

select max(sal), min(sal), round(avg(sal), 2) from emp;

select max(sal), min(sal), round(avg(sal), 2) from emp group by job;

select count(distinct mgr) from emp where mgr is not null;

select (max(sal) - min(sal)) from emp;

select min(e.sal) from emp m, emps e where m.empno = e.mgr group by m.empno;

select m.*, min(e.sal) from emp m, emp e where m.empno = e.mgr group by m.empno having min(e.sal) >= 1000;

select ename, hiredate from emp where ename not like 'BLAKE' and deptno = (select deptno from emp where ename like 'BLAKE');

select empno, ename, sal from emp where sal > (select avg(sal) from emp) and deptno in (select deptno from emp where ename like '%T%' order by deptno);