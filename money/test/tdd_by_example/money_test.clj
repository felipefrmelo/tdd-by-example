(ns tdd-by-example.money-test
  (:require [clojure.test :refer :all]
            [tdd-by-example.money :as m]
[matcher-combinators.test :refer [match?]] ))

(deftest money
  (testing "multiplication"

    (let [five (m/dollar 5)]
      (is (match? 10 (:amount (m/times five 2))))
      (is (match? 15 (:amount (m/times five 3))))
   )))
