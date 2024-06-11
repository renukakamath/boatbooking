from flask import * 
from database import*
import uuid



admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():

	return render_template('admin_home.html')
@admin.route('/admin_managestaff',methods=['post','get'])
def admin_managestaff():
	data={}
	q="select * from staff inner join login using (username)"
	res=select(q)
	
	data['staffview']=res

	if "action" in request.args:
		action=request.args['action']
		uid=request.args['uid']

		if action=='active':
			q="update login set `status`='1' where username='%s'"%(uid)
			update(q)

			q="update staff set `staff_status`='1' where username='%s'"%(uid)
			update(q)
			flash('successfully')
			return redirect(url_for('admin.admin_managestaff'))
		
		if action=='inactive':
			q="update login set `status`='0' where username='%s'"%(uid)
			update(q)
			q="update staff set `staff_status`='0' where username='%s'"%(uid)
			update(q)
			flash('successfully')
			return redirect(url_for('admin.admin_managestaff'))


		if action=='update':
			q="select * from staff"
			res=select(q)
			data['staffupdate']=res

		if "update" in request.form:
			f=request.form['fname']
			l=request.form['lname']
			d=request.form['date']
			ho=request.form['hno']
			
			ha=request.form['hna']
			
			di=request.form['district']
			p=request.form['pin']
			g=request.form['gen']
			
			
			n=request.form['num']
			
			q="update staff set staff_fname='%s',staff_lname='%s',staff_gender='%s',staff_dob='%s',staff_house_name='%s',staff_house_no='%s',staff_dist='%s',staff_pincode='%s',staff_phone='%s' where username='%s'"%(f,l,g,d,ha,ho,di,p,n,uid)
			update(q)
			print(q)
			print(q)
			flash('successfully')

			return redirect(url_for('admin.admin_managestaff'))
	

	if "staffreg" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		d=request.form['date']
		ho=request.form['hno']
		
		ha=request.form['hna']
		
		di=request.form['district']
		p=request.form['pin']
		g=request.form['gen']
		
		
		n=request.form['num']
		u=request.form['uname']
		pa=request.form['pwd']
		q="insert into login values('%s','%s','staff','1')"%(u,pa)
		insert(q)
		q="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(u,f,l,d,ho,ha,di,p,g,n)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managestaff'))


	return render_template('admin_managestaff.html',data=data)


@admin.route('/admin_managecategory',methods=['post','get'])	
def admin_managecategory():
	data={}
	q="select * from category"
	res=select(q)
	data['categoryview']=res

	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=='active':
		q="update category set status='1' where category_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecategory'))
	if action=='inactive':
		q="update category set status='0' where category_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecategory'))

	if action=='update':
		q="select * from category where category_id='%s'"%(cid)
		res=select(q)

		data['categoryupdate']=res

	if "update" in request.form:
		f=request.form['fname']

		description=request.form['description']
		
		q="update category set category_name='%s' ,cat_decription='%s' where category_id='%s'"%(f,cid,description)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecategory'))
	if "category" in request.form:
		f=request.form['fname']
		description=request.form['description']
		
		q="insert into category values(null,'%s','%s','1')"%(f,description)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecategory'))
		
	return render_template('admin_managecategory.html',data=data)

@admin.route('/admin_managesubcategory',methods=['post','get'])
def admin_managesubcategory():
	data={}
	q="select * from subcategory"
	res=select(q)
	data['subview']=res

	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']

	else:
		action=None


	if action=='active':
		q="update subcategory set sub_status='1' where subcategory_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managesubcategory'))

	if action=='inactive':
		q="update subcategory set sub_status='0' where subcategory_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managesubcategory'))

	if action=='update':
		q="select * from subcategory where subcategory_id='%s'"%(sid)
		res=select(q)
		data['subcategoryupdate']=res


	if "update" in request.form:
		f=request.form['fname']
		
		q="update subcategory set subcategory_name='%s' where subcategory_id='%s'"%(f,sid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managesubcategory'))

			
			
			

	if "subcategory" in request.form:
		f=request.form['fname']
		
		q="insert into subcategory values(null,'%s','1')"%(f)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managesubcategory'))

	return render_template('admin_managesubcategory.html',data=data)



@admin.route('/admin_manageboat',methods=['post','get'])	
def admin_manageboat():
	data={}

	q="select * from category where status='1'"
	res=select(q)
	data['categorydrop']=res

	q="select * from subcategory where sub_status='1'"
	res=select(q)
	data['subcategorydrop']=res

	


	q="SELECT * FROM boat INNER JOIN category USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) "
	res=select(q)
	data['boatview']=res



	if "action" in request.args:
		action=request.args['action']
		bid=request.args['bid']

	else:
		action=None

	if action=='available':
		q="update boat set bstatus='1' where boat_id='%s'"%(bid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_manageboat'))

	if action=='notavailable':
		q="update boat set bstatus='0' where boat_id='%s'"%(bid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_manageboat'))	

	if action=='update':
		q="SELECT * FROM boat INNER JOIN category USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`)  where boat_id='%s'"%(bid)
		res=select(q)
		
		data['boatupdate']=res


	if "update" in request.form:
		cat=request.form['cat']
		sub=request.form['subcategory']
		
		
		
		i=request.files['imgg']
		path="static/"+str(uuid.uuid4())+i.filename
		i.save(path)
		r=request.form['rate']
	
		q="update boat set category_id='%s',subcategory_id='%s',image='%s',price='%s' where boat_id='%s'"%(cat,sub,path,r,bid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_manageboat'))


	if "boat" in request.form:
		cat=request.form['cat']
		sub=request.form['subcategory']
		
		
	
		i=request.files['imgg']
		path="static/"+str(uuid.uuid4())+i.filename
		i.save(path)
		r=request.form['rate']
		
		q="insert into boat values(null,'%s','%s','%s','%s','1','1')"%(cat,sub,r,path)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_manageboat'))		


	return render_template('admin_manageboat.html',data=data)	


@admin.route('/admin_viewrating')
def admin_viewrating():
	data={}
	bid=request.args['bid']
	q="select * from rating inner join boat using (boat_id) inner join customer using (customer_id) where boat_id='%s'"%(bid)
	res=select(q)
	data['ratingview']=res
	return render_template('admin_viewrating.html',data=data)	



@admin.route('/admin_viewcustomer')	
def admin_viewcustomer():
	data={}

	if "action" in request.args:
		action=request.args['action']
		lid=request.args['lid']

	else:
		action=None

	if action=='accept':
		q="update login set status='1' where username='%s'"%(lid)
		update(q)
		q="update customer set customer_status='1' where username='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewcustomer'))

	if action=='reject':
		q="update login set status='0' where username='%s'"%(lid)
		update(q)
		q="update customer set customer_status='0' where username='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewcustomer'))
			
	q="select * from customer inner join login using (username)"
	res=select(q)
	data['customerview']=res

	return render_template('admin_viewcustomer.html',data=data)



@admin.route('/admin_viewbooking')
def admin_viewbooking():
	data={}
	q="SELECT * FROM `booking` INNER JOIN `boat` USING (`boat_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) "
	res=select(q)
	data['bookingview']=res
	return render_template('admin_viewbooking.html',data=data)	



@admin.route('/admin_viewpayment')
def admin_viewpayment():
	data={}
	bid=request.args['bid']
	q="SELECT * FROM `payment`  INNER JOIN `booking` USING (`booking_id`) INNER JOIN `customer` USING (`customer_id`) where booking_id='%s'"%(bid)
	res=select(q)
	data['paymentview']=res

	return render_template('admin_viewpayment.html',data=data)	


@admin.route('/admin_managereport',methods=['post','get'])	
def admin_managereport():
	data={}
	if "sale" in request.form:
		daily=request.form['daily']
		if request.form['monthly']=="":
			monthly=""
		else:
			monthly=request.form['monthly']+'%'
		print(monthly)
		customer=request.form['customer']	
		q="SELECT * FROM `booking` INNER JOIN `boat` USING (`boat_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) where (`customer_fname` like '%s') or (`date` like '%s'  ) or (`date` like '%s' ) "%(customer,daily,monthly)
		res=select(q)
		print(q)
		data['report']=res
		session['res']=res
		r=session['res']
	else:
		q="SELECT * FROM `booking` INNER JOIN `boat` USING (`boat_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`)"
		res=select(q)
		data['report']=res
	
	return render_template('admin_managereport.html',data=data)

@admin.route('/admin_salesreport')
def admin_salesreport():
	data={}

	r=session['res']
	data['r']=r


	return render_template('admin_salesreport.html',data=data)	






