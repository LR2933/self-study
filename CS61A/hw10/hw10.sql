CREATE TABLE parents (parent TEXT, child TEXT);

INSERT INTO parents VALUES
  ('ace', 'bella'),
  ('ace', 'charlie'),
  ('daisy', 'hank'),
  ('finn', 'ace'),
  ('finn', 'daisy'),
  ('finn', 'ginger'),
  ('ellie', 'finn');

CREATE TABLE dogs (name TEXT, fur TEXT, height INTEGER);

INSERT INTO dogs VALUES
  ('ace',     'long',  26),
  ('bella',   'short', 52),
  ('charlie', 'long',  47),
  ('daisy',   'long',  46),
  ('ellie',   'short', 35),
  ('finn',    'curly', 32),
  ('ginger',  'short', 28),
  ('hank',    'curly', 31);

CREATE TABLE sizes (size TEXT, min INTEGER, max INTEGER);

INSERT INTO sizes VALUES
  ('toy',      24, 28),
  ('mini',     28, 35),
  ('medium',   35, 45),
  ('standard', 45, 60);


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  select child from parents inner join dogs on parents.parent = dogs.name order by dogs.height desc;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size from dogs inner join sizes on (dogs.height > sizes.min and dogs.height <= sizes.max);


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  select p1.child as first_child, p2.child as second_child, s1.size as size 
    from parents p1 inner join parents p2 on p1.parent = p2.parent and p1.child != p2.child 
        inner join size_of_dogs s1 inner join size_of_dogs s2 on s1.name = p1.child and s2.name = p2.child and s1.size = s2.size 
    where p1.child < p2.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  select "The two siblings, " || first_child || " and " || second_child || ", have the same size: " || size
    from siblings;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  select fur, max(height) - min(height) as height_range
    from dogs group by fur having min(height) >= avg(height) * 0.7 and max(height) < avg(height) * 1.3;

