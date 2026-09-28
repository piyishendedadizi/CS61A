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
  SELECT child from parents join dogs on dogs.name = parents.parent ORDER BY height DESC;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size from dogs join sizes on dogs.height > sizes.min and dogs.height <= sizes.max;


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT parents1.child as child1, parents2.child as child2, dogs1.height as height1, dogs2.height as height2, sizes1.size as sizes1, sizes2.size as sizes2
  from parents as parents1 
  join parents as parents2 on parents1.parent = parents2.parent and parents1.child != parents2.child 
  join dogs as dogs1 on dogs1.name = parents1.child
  join dogs as dogs2 on dogs2.name = parents2.child
  join sizes as sizes1 on dogs1.height > sizes1.min and dogs1.height <= sizes1.max
  join sizes as sizes2 on dogs2.height > sizes2.min and dogs2.height <= sizes2.max
  where parents1.child < parents2.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || child1 || " and " || child2 || ", have the same size: " || sizes1
  from siblings
  where sizes1 = sizes2;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE avgs AS
  SELECT d.name, d.fur, a.avg_h
  FROM dogs AS d
  JOIN (SELECT fur, AVG(height) AS avg_h FROM dogs GROUP BY fur) AS a
  ON d.fur = a.fur;


CREATE TABLE low_variance1 AS
  SELECT avgs.fur, avgs.avg_h, MAX(dogs.height) as max, MIN(dogs.height) as min
  from avgs
  join dogs on dogs.name = avgs.name
  GROUP BY avgs.fur;

CREATE TABLE low_variance AS
  SELECT fur, max - min as height_range
  from low_variance1
  where min >= avg_h * 0.7 AND max <= avg_h * 1.3;