(ns aoc.day1
  (:require [clojure.math.combinatorics :refer [combinations]]
            [clojure.test :refer [deftest testing is run-tests]]))

;; Solution

(defn- sum-equals? [number]
  (fn [numbers] (= number (apply + numbers))))

(defn solve [data tuple-size]
  (->> (combinations data tuple-size)
       (filter (sum-equals? 2020))
       first
       (apply *)))


;; Verification

(deftest day-1-verification
  (let [example-data [1721 979 366 299 675 1456]]
    (testing "Part One"
      (is (= (solve example-data 2) 514579)))
    (testing "Part Two"
      (is (= (solve example-data 3) 241861950)))))

(run-tests)
