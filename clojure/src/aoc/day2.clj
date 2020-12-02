(ns aoc.day2
  (:require [clojure.test :refer [deftest testing is run-tests]]
            [clojure.string :refer [split-lines]]))

(def example-data ["1-3 a: abcde"
                   "1-3 b: cdefg"
                   "2-9 c: ccccccccc"])
(def day2-data (split-lines (slurp "data/day2.data")))
(def pattern #"^(\d+)-(\d+) (\w+):\s(.+)\s*$")

(defn- parse-line [line]
  (let [[_ number-1 number-2 character password] (re-matches pattern line)]
    [(Integer/parseInt number-1)
     (Integer/parseInt number-2)
     (.charAt character 0)
     password]))

(defn- validate-part1 [[min max character password]]
  (let [count (get (frequencies password) character 0)]
    (and (>= count min)
         (<= count max))))

(defn- nth-chars [indexes string]
  (map #(nth string (dec %)) indexes))

(defn- validate-part2 [[pos-1 pos-2 character password]]
  (->> password
       (nth-chars [pos-1 pos-2])
       (filter (partial = character))
       count
       (= 1)))
    

(defn solve
  "Day2.1: Find number of password(s) compliant with their policy"
  [data validator]
  (->> data
       (map parse-line)
       (filter validator)
       count))

(deftest day-2-verification
  (testing "Part One"
    (is (= (solve example-data validate-part1) 2))
    (is (= (solve day2-data validate-part1) 569)))
  (testing "Part Two"
    (is (= (solve example-data validate-part2) 1))
    (is (= (solve day2-data validate-part2) 346))))

(run-tests)