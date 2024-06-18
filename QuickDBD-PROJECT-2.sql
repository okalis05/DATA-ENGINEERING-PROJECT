-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/aLUX0R
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "movie" (
    "Title_ID" varchar(10)   NOT NULL,
    "Titles" varchar(255)   NOT NULL,
    "Categories" varchar(20)   NOT NULL,
    "Date_Added" date   NOT NULL,
    "Ratings" varchar(10)   NOT NULL
);

CREATE TABLE "titles" (
    "Show_ID" varchar(10)   NOT NULL,
    "Titles_ID" varchar(10)   NOT NULL,
    "Categories" varchar(20)   NOT NULL,
    "Titles" varchar(255)   NOT NULL,
    CONSTRAINT "pk_titles" PRIMARY KEY (
        "Show_ID","Titles_ID"
     )
);

CREATE TABLE "netflix" (
    "Show_ID" varchar(10)   NOT NULL,
    "Titles" varchar(255)   NOT NULL,
    "Categories" varchar(20)   NOT NULL,
    "Date_Added" date   NOT NULL,
    "Ratings" varchar(10)   NOT NULL,
    "Directors" varchar(255)   NOT NULL,
    CONSTRAINT "pk_netflix" PRIMARY KEY (
        "Show_ID"
     )
);

CREATE TABLE "director" (
    "IDs" int   NOT NULL,
    "Titles" varchar(255)   NOT NULL,
    "First_Name" varchar(255)   NOT NULL,
    "Last_Name" varchar(255)   NOT NULL,
    "Show_ID" varchar(10)   NOT NULL,
    "Categories" varchar(20)   NOT NULL,
    "Date_Added" date   NOT NULL,
    CONSTRAINT "pk_director" PRIMARY KEY (
        "IDs","Show_ID"
     )
);

ALTER TABLE "movie" ADD CONSTRAINT "fk_movie_Title_ID" FOREIGN KEY("Title_ID")
REFERENCES "titles" ("Show_ID");

ALTER TABLE "titles" ADD CONSTRAINT "fk_titles_Show_ID" FOREIGN KEY("Show_ID")
REFERENCES "netflix" ("Show_ID");

ALTER TABLE "director" ADD CONSTRAINT "fk_director_Show_ID" FOREIGN KEY("Show_ID")
REFERENCES "netflix" ("Show_ID");

