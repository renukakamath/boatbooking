from flask import *
from database import*


public=Blueprint('public',__name__)

@public.route('/')
def public_home():


	return render_template('public_home.html')

@public.route('/public_login',methods=['post','get'])
def public_login():
	if "login" in request.form:
		u=request.form['uname']
		p=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,p)
		res=select(q)
		if res:
			session['username']=res[0]['username']
			lid=session['username']

			if res[0]['user_type']=="admin":
				session['type']="admin"
				return redirect(url_for('admin.admin_home'))
			elif res[0]['user_type']=="customer":
				q="select * from customer inner join login using (username) where username='%s' and status='0'"%(u)
				res=select(q)
				if res:
					flash('inactive')
				else:


					q="select * from customer where username='%s'"%(lid)
					res=select(q)
					if res:
						session['customer_id']=res[0]['customer_id']
						cid=session['customer_id']
						session['type']="customer"
					return redirect(url_for('customer.customer_home'))
			elif res[0]['user_type']=="staff":
				q="select * from staff inner join login using (username) where username='%s' and status='0'"%(u)
				res=select(q)
				if res:
					flash('inactive')
				else:
					q="select * from staff where username='%s'"%(lid)
					res=select(q)
					if res:
						session['staff_id']=res[0]['staff_id']
						sid=session['staff_id']
						session['type']="staff"
					return redirect(url_for('staff.staff_home'))

		else:
			flash('invalid username and password')

			

		
	return render_template('public_login.html')


@public.route('/customer_registration',methods=['post','get'])	
def customer_registration():
	if "cusreg" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		h=request.form['hno']
		
		di=request.form['district']
		
		pi=request.form['pin']
		
		n=request.form['num']
		
		u=request.form['uname']
		pa=request.form['pwd']


		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:

			flash('already exist')

		else:
			
			q="insert into login values('%s','%s','customer','1')"%(u,pa)
			insert(q)
			q="insert into customer values(null,'%s','%s','%s','%s','%s','%s','%s','1')"%(u,f,l,h,di,pi,n)
			insert(q)
			print(q)
			flash('successfully')
			return redirect(url_for('public.customer_registration'))

	return render_template('customer_registration.html')

		