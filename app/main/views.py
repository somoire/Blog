from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PostForm,SubscriberForm,CommentForm
from ..import db,photos
from ..models import User,Post,Role,Subscriber,Comment
from flask_login import login_required,current_user
import markdown2
from ..email import mail_message

#Views
@main.route("/",methods=['GET','POST'])
def index():
    """
    View root page function that returns the index page and its data
    """
    posts = Post.query.all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('index.html',title=title,posts=posts,subscriber_form=form)

@main.route("/new_post",methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        like=0
        new_post=Post(title=title,post=post,category=category,like=like)

        new_post.save_post()

        subscribers=Subscriber.query.all()

        for subscriber in subscribers:
            mail_message("New Blog Post","email/new_post",subscriber.email,post=new_post)

        return redirect(url_for('main.index'))

    title="Make a post"
    return render_template('new_post.html',title=title,post_form=form)

@main.route("/post/<int:id>",methods=['GET','POST'])
def post(id):
    post=Post.query.get_or_404(id)
    comment = Comment.query.all()
    form=CommentForm()

    if request.args.get("like"):
        post.like = post.like+1

        db.session.add(post)
        db.session.commit()

        return redirect("/post/{post_id}".format(post_id=post.id))

    if form.validate_on_submit():
        comment=form.comment.data
        new_comment = Comment(id=id,comment=comment,user_id=current_user.id,post_id=post.id)

        new_comment.save_comment()

        return redirect("/post/{post_id}".format(post_id=post.id))

    return render_template('post.html',post=post,comments=comment,comment_form=form)
@main.route("/life",methods=['GET','POST'])
def life():
    """
    View root page function that returns the index page and its data
    """
    posts = Post.query.filter_by(category="Life").all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('life.html',title=title,posts=posts,subscriber_form=form)
@main.route("/culture",methods=['GET','POST'])
def culture():
    """
    View root page function that returns the index page and its data
    """
    posts = Post.query.filter_by(category="Culture").all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('culture.html',title=title,posts=posts,subscriber_form=form)

@main.route("/fashion",methods=['GET','POST'])
def fashion():
    """
    View root page function that returns the index page and its data
    """
    posts = Post.query.filter_by(category="Fashion").all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('fashion.html',title=title,posts=posts,subscriber_form=form)

@main.route("/fatherhood",methods=['GET','POST'])
def fatherhood():
    """
    View root page function that returns the index page and its data
    """
    posts = Post.query.filter_by(category="Fatherhood").all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('fatherhood.html',title=title,posts=posts,subscriber_form=form)

@main.route("/food",methods=['GET','POST'])
def food():
    """
    View root page function that returns the index page and its data
    """
    posts = Post.query.filter_by(category="Food").all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('food.html',title=title,posts=posts,subscriber_form=form)

@main.route("/people",methods=['GET','POST'])
def people():
    """
    View root page function that returns the index page and its data
    """
    posts = Post.query.filter_by(category="People").all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('people.html',title=title,posts=posts,subscriber_form=form)

@main.route("/tech",methods=['GET','POST'])
def tech():
    """
    View root page function that returns the index page and its data
    """
    posts = Post.query.filter_by(category="Tech").all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('tech.html',title=title,posts=posts,subscriber_form=form)

@main.route("/travel",methods=['GET','POST'])
def travel():
    """
    View root page function that returns the index page and its data
    """
    posts = Post.query.filter_by(category="Travel").all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('travel.html',title=title,posts=posts,subscriber_form=form)
