create trigger score_increment 
after insert on BookReview
for each row
begin
	if BooReview.score = 10 then
		update BookAuthor 
			set earnings = earnings + 100 
			where BookAuthor.book = BookReview.book ;
	-- needs a rollback inside an if just here for Part 1 b) but where is coauthor?
	end if ;
end ;


-- This is a hunch. Need to see "previous assignment (#9) Question (a)""
create trigger delete_cascade
before delete on BookPublish
begin
	delete from BookAuthor where BookAuthor.book = BookPublish.book ;
	delete from BookReference where BookReference.book = BookPublish.book ;
	delete from BookReview where BookReview.book = BookPublish.book ;
end ;